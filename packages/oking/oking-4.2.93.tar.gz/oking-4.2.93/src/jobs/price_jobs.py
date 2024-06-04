import logging
from typing import List
import threading

import src.database.connection as database
import src.database.utils as utils
from src.api.entities.preco_lista import ListaPreco, Escopo
from src.api.entities.preco_okvendas import Preco_OkVendas
from src.database.entities.price_list import DbPriceList, PriceListProduct
from src.database.queries import IntegrationType
from src.database.utils import DatabaseConfig
import src.api.okinghub as api_okHUB
import src.api.api_mplace as api_Mplace
import src.api.okvendas as api_okVendas
from src.database import queries
import src
from threading import Lock

from src.jobs.system_jobs import OnlineLogger
from src.jobs.utils import executa_comando_sql

logger = logging.getLogger()
send_log = OnlineLogger.send_log
lock = Lock()


def job_send_prices(job_config_dict: dict):
    """
    Job para realizar a atualização de preços
    Args:
        job_config_dict: Configuração do job
    """
    with lock:
        global lista_preco
        db_config = utils.get_database_config(job_config_dict)
        # Exibe mensagem monstrando que a Thread foi Iniciada
        logger.info(f'==== THREAD INICIADA -job: ' + job_config_dict.get('job_name'))

        # LOG de Inicialização do Método - Para acompanhamento de execução
        send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), True,
                 f'Preço - Iniciado', 'exec', 'envia_preco_job', 'PRECO')

        if job_config_dict['executar_query_semaforo'] == 'S':
            executa_comando_sql(db_config, job_config_dict)

        send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), False,
                 f'Operação' + src.client_data['operacao'].lower(), 'exec', 'envia_preco_job', 'PRECO')
        try:

            if src.client_data['operacao'].lower().__contains__('okvendas'):
                prices = query_prices_okvendas(job_config_dict, db_config)
            else:
                prices = query_prices_erp(job_config_dict, db_config)

            if prices is not None and len(prices) > 0:
                send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), True,
                         f'Total de Preço(s) a serem atualizados: {len(prices)}', 'info', 'PRECO', 'PRECO')

                api_prices = []
                for price in prices:
                    if api_prices.__len__() < 50:
                        api_prices.append(price)
                    else:
                        send_log(job_config_dict.get('job_name'), False, False,
                                 f'Enviando Pacote: {api_prices.__len__()}',
                                 'info', 'PRECO', '')
                        if src.client_data['operacao'].lower().__contains__('okvendas'):
                            logger.info("== Okvendas - Entrou no if Post ==")
                            response = api_okVendas.post_prices(api_prices)
                            send_log(job_config_dict.get('job_name'), False, False, f'Tratando retorno', 'info',
                                     'PRECO',
                                     '')
                            lista_preco = price.lista_preco

                            validade_response_price(response, "", db_config, job_config_dict)
                        elif src.client_data['operacao'].lower().__contains__('okinghub'):
                            logger.info("== OkingHub - Entrou no if Post ==")
                            response = api_okHUB.post_prices(api_prices)
                            send_log(job_config_dict.get('job_name'), False, False, f'Tratando retorno', 'info',
                                     'PRECO',
                                     '')
                            validade_response_price(response, "", db_config, job_config_dict)
                        else:
                            logger.info("== MPlace - Entrou no if Post ==")
                            api_Mplace.put_prices_mplace(api_prices, db_config, job_config_dict)
                        api_prices = []

                # Se ficou algum sem processa
                if api_prices.__len__() > 0:
                    send_log(job_config_dict.get('job_name'), False, False,
                             f'Enviando Pacote: {api_prices.__len__()}',
                             'info', 'PRECO', '')
                    if src.client_data['operacao'].lower().__contains__('okvendas'):
                        logger.info("== Okvendas - Entrou no if Post ==")
                        response = api_okVendas.post_prices(api_prices)
                        send_log(job_config_dict.get('job_name'), False, False, f'Tratando retorno', 'info',
                                 'PRECO',
                                 '')
                        lista_preco = price.lista_preco

                        validade_response_price(response, "", db_config, job_config_dict)
                    elif src.client_data['operacao'].lower().__contains__('okinghub'):
                        logger.info("== OkingHub - Entrou no if Post ==")
                        response = api_okHUB.post_prices(api_prices)
                        send_log(job_config_dict.get('job_name'), False, False, f'Tratando retorno', 'info',
                                 'PRECO',
                                 '')
                        validade_response_price(response, "", db_config, job_config_dict)
                    else:
                        logger.info("== MPlace - Entrou no if Post ==")
                        api_Mplace.put_prices_mplace(api_prices, db_config, job_config_dict)

            else:
                send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), True
                         , f'Nao existem precos a serem enviados no momento', 'warning', 'PRECO')
        except Exception as e:
            send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), True
                     , f'Erro durante execucao do job: {str(e)}', 'error', 'envia_preco_job', 'PRECO')


def query_prices_erp(job_config_dict: dict, db_config: DatabaseConfig):
    """
    Consulta os precos para atualizar no banco de dados
    Args:
        job_config_dict: Configuração do job
        db_config: Configuracao do banco de dados

    Returns:
        Lista de preços para atualizar
    """
    db = database.Connection(db_config)
    conn = db.get_conect()
    cursor = conn.cursor()
    try:
        # monta query com EXISTS e NOT EXISTS
        # verificar se já possui WHERE
        newsql = utils.final_query(db_config)
        conexao = database.Connection(db_config)
        conn = conexao.get_conect()
        if src.print_payloads:
            print(newsql)
        cursor.execute(newsql.lower())
        rows = cursor.fetchall()
        columns = [col[0].lower() for col in cursor.description]
        results = list(dict(zip(columns, row)) for row in rows)
        cursor.close()
        conn.close()

        prices = []
        if len(results) > 0:
            prices = price_dict(results)
        return prices

    except Exception as ex:
        send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), True,
                 f' Erro ao consultar precos no banco semaforo: {str(ex)}', 'error', 'PRECO')
        if src.exibir_interface_grafica:
            raise


def query_prices_okvendas(job_config_dict: dict, db_config: DatabaseConfig) -> List[Preco_OkVendas]:
    """
    Consulta os precos para atualizar no banco de dados
    Args:
        job_config_dict: Configuração do job
        db_config: Configuracao do banco de dados

    Returns:
        Lista de preços para atualizar
    """
    db = database.Connection(db_config)
    conn = db.get_conect()
    cursor = conn.cursor()
    try:
        newsql = utils.final_query(db_config)

        if src.print_payloads:
            print(newsql)

        cursor.execute(newsql)
        rows = cursor.fetchall()
        columns = [col[0].lower() for col in cursor.description]
        results = list(dict(zip(columns, row)) for row in rows)
        cursor.close()
        conn.close()

        send_log(job_config_dict.get('job_name'), False, False, f'== Executou a query', 'info', 'PRECO', '')
        if len(results) > 0:
            prices = [Preco_OkVendas(**p) for p in results]
            return prices

    except Exception as ex:
        send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), True,
                 f' Erro ao consultar precos no banco semaforo: {str(ex)}', 'error', 'PRECO')

    return []


def price_dict(prices):
    lista = []
    if src.client_data['operacao'].lower().__contains__('mplace'):
        for row in prices:
            pdict = {
                'marketplace_scope_code': str(row['lista_preco']),
                'erp_code': str(row['sku']),
                'variation_option_id': str(row['variation_option_id']),
                'sale_price': float(row['preco_por']),
                'list_price': float(row['preco_de']),
                'ipi_value': float(row['ipi']),
                'st_value': float(row['st'])
            }
            lista.append(pdict)
    else:
        for row in prices:
            pdict = {
                'sku': str(row['sku']),
                'lista_preco': str(row['lista_preco']),
                'preco_de': float(row['preco_de']),
                'preco_por': float(row['preco_por']),
                'token': str(src.client_data.get('token_oking')),
            }
            lista.append(pdict)
    return lista


def validade_response_price(response, lista_scope_code, db_config, job_config_dict):
    if response is not None:
        logger.info("== Validate Response ==")
        conexao = database.Connection(db_config)
        conn = conexao.get_conect()
        cursor = conn.cursor()
        sucesso = None
        # Percorre todos os registros
        for item in response:
            if src.client_data['operacao'].lower().__contains__('mplace'):
                logger.info(" == Mplace - Preenchendo valores para a semáforo ==")
                identificador = item.erp_code
                identificador2 = lista_scope_code
                sucesso = item.sucesso
                mensagem = item.mensagem

            elif src.client_data['operacao'].lower().__contains__('okvendas'):
                logger.info(" == Okvendas - Preenchendo valores para a semáforo ==")
                identificador = item.Identifiers[0]
                identificador2 = lista_preco
                sucesso = item.Status
                mensagem = item.Message

            else:
                logger.info(" == OkingHub - Preenchendo valores para a semáforo ==")
                identificador = item.identificador
                identificador2 = item.identificador2
                sucesso = item.sucesso
                mensagem = item.mensagem

            if sucesso:
                msgret = 'SUCESSO'
            else:
                msgret = mensagem
                send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), True,
                         f'Mensagem de Retorno: {identificador}, {msgret}', 'warning',
                         'PRECO', identificador)
            # Mesmo se der erro retira da Fila, mas grava a mensagem no Banco
            try:
                logger.info(f"== Antes de executar inserção na tabela Semaforo: {identificador}, {identificador2}, {IntegrationType.PRECO.value}, {msgret}")
                cursor.execute(queries.get_insert_update_semaphore_command(db_config.db_type),
                               queries.get_command_parameter(db_config.db_type
                                                             , [identificador, identificador2
                                                                 , IntegrationType.PRECO.value
                                                                 , msgret]))
                # atualizados.append(response['identificador'])
            except Exception as e:
                send_log(job_config_dict.get('job_name')
                         , job_config_dict.get('enviar_logs')
                         , True
                         , f'Erro ao atualizar Preço do sku: {identificador}, Erro: {str(e)}'
                         , 'error'
                         , 'PRECO'
                         , f'{identificador}-{identificador2}')

        cursor.close()
        conn.commit()
        conn.close()


def job_prices_list(job_config_dict: dict):
    """
        Job para integrar listas de preço com o okvendas

        Args:
            job_config_dict: Configuração do job
        """
    with lock:
        logger.info(f'==== THREAD INICIADA -job: ' + job_config_dict.get('job_name'))
        # LOG de Inicialização do Método - Para acompanhamento de execução
        send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), True,
                 f'Lista de Preço - Iniciado', 'exec', 'job_prices_list', 'PRECO')
        db_config = utils.get_database_config(job_config_dict)
        # Executa o Comando da Semaforo Antes do Query Principal
        if job_config_dict['executar_query_semaforo'] == 'S':
            logger.info(f'Executando a query semáforo')
            executa_comando_sql(db_config, job_config_dict)

        if db_config.sql is None:
            send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), False,
                     f'Comando sql para listas de preco nao encontrado', 'warning', 'PRECO')
            return

        try:
            send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), False,
                     f'Consultando listas de preco no banco semaforo', 'info', 'PRECO')
            duplicated_db_price_lists = query_price_lists(job_config_dict, db_config)

            # Carrega no dict todas as listas de preço agrupando pelo codigo da lista de preco e incrementando a lista de clientes
            unique_api_price_lists = dict.fromkeys(set([d.price_list_code for d in duplicated_db_price_lists]))
            unique_db_price_lists = dict.fromkeys(set([d.price_list_code for d in duplicated_db_price_lists]))
            for d in duplicated_db_price_lists:
                if unique_db_price_lists[d.price_list_code] is None:
                    unique_db_price_lists[d.price_list_code] = d

                if unique_api_price_lists[d.price_list_code] is None:
                    unique_api_price_lists[d.price_list_code] = ListaPreco(d.price_list_description, d.price_list_code,
                                                                           d.branch_code, d.initial_date, d.final_date,
                                                                           d.active, d.priority,
                                                                           Escopo(d.scope_type, [d.client_code]),
                                                                           d.calculate_ipi)
                else:
                    if not unique_api_price_lists[d.price_list_code].escopo.codigos_escopo.__contains__(d.client_code):
                        unique_api_price_lists[d.price_list_code].escopo.codigos_escopo.append(d.client_code)

            db_price_lists = list(unique_db_price_lists.values())
            send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), False,
                     f'Inserindo/atualizando listas de preco no banco semaforo: {len(db_price_lists)}', 'info', 'PRECO')
            if not insert_update_semaphore_price_lists(job_config_dict, db_config, db_price_lists):
                send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), False,
                         f'Nao foi possivel inserir as listas de preco no banco semaforo', 'error', 'PRECO')
                return

            api_price_lists: List[ListaPreco] = list(unique_api_price_lists.values())
            for api_price_list in api_price_lists:
                try:
                    response_list = api_okVendas.put_price_lists([api_price_list])
                    for res in response_list:
                        if res.status != 1:
                            send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), False,
                                     f'Erro ao processar lista de preco {api_price_list.codigo_lista_preco}: {res.message}',
                                     'warning', 'PRECO')

                        if protocol_semaphore_item(job_config_dict, db_config, api_price_list.codigo_lista_preco, None):
                            send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), False,
                                     f'Lista de preco {api_price_list.codigo_lista_preco} protocolado no banco semaforo',
                                     'info', 'PRECO')
                        else:
                            send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), False,
                                     f'Falha ao protocolar a lista de preco {api_price_list.codigo_lista_preco}',
                                     'warning',
                                     'PRECO')

                except Exception as e:
                    send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), True,
                             f'Falha no envio da lista de preco {api_price_list.codigo_lista_preco}: {str(e)}', 'error',
                             'PRECO')

        except Exception as ex:
            send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), True, f'Erro {str(ex)}',
                     'error',
                     'PRECO')


def query_price_lists(job_config_dict: dict, db_config: DatabaseConfig) -> List[DbPriceList]:
    """
    Consulta os listas de precos para consultar no banco de dados
    Args:
        job_config_dict: Configuração do job
        db_config: Configuracao do banco de dados

    Returns:
        Lista de preços para atualizar
    """
    db = database.Connection(db_config)
    conn = db.get_conect()
    cursor = conn.cursor()
    try:
        if src.print_payloads:
            print(db_config.sql)
        cursor.execute(db_config.sql)
        rows = cursor.fetchall()
        columns = [col[0].lower() for col in cursor.description]
        results = list(dict(zip(columns, row)) for row in rows)
        cursor.close()
        conn.close()
        if len(results) > 0:
            # print(results)
            lists = [DbPriceList(**p) for p in results]
            return lists

    except Exception as ex:
        send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), True,
                 f' Erro ao consultar listas de precos: {str(ex)}', 'error', 'PRECO')

    return []


def insert_update_semaphore_price_lists(job_config_dict: dict, db_config: DatabaseConfig,
                                        lists: List[DbPriceList]) -> bool:
    """
    Consulta os listas de precos para consultar no banco de dados
    Args:
        job_config_dict: Configuração do job
        db_config: Configuracao do banco de dados
        lists: Lista de listas de preço

    Returns:
        Boleano indicando se foram inseridos 1 ou mais registros
    """

    try:
        params = [(li.price_list_code, ' ', IntegrationType.LISTA_PRECO.value, 'SUCESSO') for li in lists]
        send_log(job_config_dict.get('job_name'), False, False, f'Quantidade de Parâmetros: {params.__len__()}', 'info',
                 'PRECO')
        db = database.Connection(db_config)
        conn = db.get_conect()
        cursor = conn.cursor()
        for p in params:
            print(list(p))
            cursor.execute(queries.get_insert_update_semaphore_command(db_config.db_type),
                           queries.get_command_parameter(db_config.db_type, list(p)))
        count = cursor.rowcount
        cursor.close()
        conn.commit()
        conn.close()

        return count > 0

    except Exception as ex:
        send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), True,
                 f' Erro ao ATUALIZAR Capa listas de precos no banco semaforo: {str(ex)}', 'error', 'PRECO')

    return False


def protocol_semaphore_item(job_config_dict: dict, db_config: DatabaseConfig, identifier: str,
                            identifier2: str) -> bool:
    db = database.Connection(db_config)
    conn = db.get_conect()
    cursor = conn.cursor()
    try:
        if identifier2 is None:
            cursor.execute(queries.get_protocol_semaphore_id_command(db_config.db_type),
                           queries.get_command_parameter(db_config.db_type, ['SUCESSO', identifier]))
        else:
            cursor.execute(queries.get_protocol_semaphore_id2_command(db_config.db_type),
                           queries.get_command_parameter(db_config.db_type, ['SUCESSO', identifier, identifier2]))
        count = cursor.rowcount
        cursor.close()
        conn.commit()
        conn.close()
        return count > 0

    except Exception as ex:
        send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), True,
                 f' Erro ao protocolar item no banco semaforo: {str(ex)}', 'error', 'PRECO')


def job_products_prices_list(job_config_dict: dict):
    with lock:
        """
            Job para inserir a relação de produtos com as listas de preço no banco semáforo

            Args:
                job_config_dict: Configuração do job
            """
        logger.info(f'==== THREAD INICIADA -job: ' + job_config_dict.get('job_name'))
        # LOG de Inicialização do Método - Para acompanhamento de execução
        send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), True,
                 f'Lista Preço do Produto em Lote - Iniciado', 'exec', 'job_products_prices_list', 'PRECO')
        db_config = utils.get_database_config(job_config_dict)
        # Executa o Comando da Semaforo Antes do Query Principal
        if job_config_dict['executar_query_semaforo'] == 'S':
            logger.info(f'Executando a query semáforo')
            executa_comando_sql(db_config, job_config_dict)
        if db_config.sql is None:
            send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), False,
                     f'Comando sql para inserir a relação de produtos com as listas de preco no semaforo nao encontrado',
                     'warning', 'PRECO')
            return
        if job_config_dict['executar_query_semaforo'] == 'S':
            executa_comando_sql(db_config, job_config_dict)
        try:
            db_price_list_products = query_price_list_products(job_config_dict, db_config)

            if not insert_update_semaphore_price_lists_products(job_config_dict, db_config, db_price_list_products):
                send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), False
                         , f'Nao foi possivel inserir os produtos das listas de preco no banco semaforo', 'error',
                         'PRECO')
                return

            split_price_lists = dict.fromkeys(set([d.price_list_code for d in db_price_list_products]), [])
            for prod in db_price_list_products:
                split_price_lists[prod.price_list_code].append(
                    PriceListProduct(prod.price_list_code, prod.erp_code, prod.price, prod.price_from, prod.other_price,
                                     prod.ipi))

            for k, v in split_price_lists.items():
                products_file = mount_price_list_products_file(v)
                if not api_okVendas.put_price_lists_products(k, products_file):
                    send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), False,
                             f'Erro ao processar lista de preco {k}', 'warning', 'PRECO')

            for prod in db_price_list_products:
                if protocol_semaphore_item(job_config_dict, db_config, prod.price_list_code, prod.erp_code):
                    send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), False,
                             f'Produto {prod.erp_code} da lista de preco {prod.price_list_code} protocolado no banco semaforo',
                             'info', 'PRECO')
                else:
                    send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), False,
                             f'Falha ao protocolar o produto {prod.erp_code} da lista de preco {prod.price_list_code}',
                             'warning', 'PRECO')

        except Exception as ex:
            send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), True, f'Erro {str(ex)}',
                     'error', 'PRECO')


def query_price_list_products(job_config_dict: dict, db_config: DatabaseConfig) -> List[PriceListProduct]:
    """
        Consultar no banco semáforo a lista de produtos relacionados a lista de preço

        Args:
            job_config_dict: Configuração do job
            db_config: Configuração do banco de dados

        Returns:
        Lista de produtos relacionados a lista de preço informada
        """
    db = database.Connection(db_config)
    conn = db.get_conect()
    cursor = conn.cursor()

    if src.print_payloads:
        print("=====================================================================")
        print(db_config.sql)
    try:
        cursor.execute(db_config.sql)
        rows = cursor.fetchall()
        if src.print_payloads:
            print(f" Linhas Retornadas: {len(rows)} ")
        columns = [col[0].lower() for col in cursor.description]
        results = list(dict(zip(columns, row)) for row in rows)
        cursor.close()
        conn.close()
        if len(results) > 0:
            if src.print_payloads:
                print(f" Registros: {len(results)} ")
            lists = [PriceListProduct(**p) for p in results]
            return lists

    except Exception as ex:
        send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), True
                 , f' Erro ao consultar produtos da lista de preco no banco semaforo: {str(ex)}'
                 , 'error', 'PRODUTO_LISTA_PRECO_JOB', 'LISTA DE PREÇO')

    return []


def mount_price_list_products_file(products: List[PriceListProduct]) -> str:
    file: str = ''
    for p in products:
        file += f'{p.price_list_code},{p.erp_code},{p.price},{p.price_from},{p.other_price},{p.ipi}\n'

    return file


def insert_update_semaphore_price_lists_products(job_config_dict: dict, db_config: DatabaseConfig,
                                                 lists: List[PriceListProduct]) -> bool:
    """
    Consulta os listas de precos para consultar no banco de dados
    Args:
        job_config_dict: Configuração do job
        db_config: Configuracao do banco de dados
        lists: Lista de produtos de um(as) listas de preço

    Returns:
        Boleano indicando se foram inseridos 1 ou mais registros
    """
    params = [(li.price_list_code, li.erp_code, IntegrationType.LISTA_PRECO_PRODUTO.value, 'SUCESSO') for li in lists]

    db = database.Connection(db_config)
    conn = db.get_conect()
    cursor = conn.cursor()
    try:
        if src.print_payloads:
            print(f" Parametros da Lista de Preço-Semaforo: {params} ")

        for p in params:
            cursor.execute(queries.get_insert_update_semaphore_command(db_config.db_type),
                           queries.get_command_parameter(db_config.db_type, list(p)))
        count = cursor.rowcount
        cursor.close()
        conn.commit()
        conn.close()
        return count > 0

    except Exception as ex:
        if src.print_payloads:
            print(f"Erro na Lista de Preço-Semaforo: {ex}")
        send_log(job_config_dict.get('job_name'), job_config_dict.get('enviar_logs'), True
                 , f' Erro ao consultar listas de precos no banco semaforo: {str(ex)}', 'error'
                 , 'PRODUTO_LISTA_PRECO_JOB', 'LISTA DE PREÇO')

    return False
