import json
import httpx
from datetime import datetime, timedelta, timezone

class errorAnymarket:
    msg = None
    statuscode = None
    def __init__(self, msg, statuscode) -> None:
        self.msg = msg
        self.statuscode = statuscode
        
    @staticmethod
    def throwError(msg, statuscode):
        if msg is not None and statuscode is not None:
            return f'Status code: {statuscode} \n message: {msg}'

class Pedido:
    token = None
        
    def _trataRetorno(self, params, response, listOrders):
        if response.status_code == 200: 
            data = {}
            response.encoding = 'utf-8'
            responsedict = json.loads(response.text)
            totalPaginas = responsedict['page']['totalPages']
            content = responsedict.get('content', None)
            if content is not None:
                data = {
                    'createdAfter': f'{params["createdAfter"]}',
                    'createdBefore': f'{params["createdBefore"]}',
                    'offset': f'{params["offset"]}',
                    'content': content
                }
                listOrders['orders'].append(data)
                return totalPaginas
            else:
                return None
        else:
            errorMsg = errorAnymarket.throwError(response.text, response.status_code)    
            print(errorMsg)

    def _requisicao(self, token, params, listOrders):
        endpoint = 'http://api.anymarket.com.br/v2/orders'
        response = httpx.get(endpoint, headers={f'gumgaToken': token}, params=params, timeout=None)
        # print(f'response.text: {response.text}')
        
        totalPaginas = self._trataRetorno(params, response, listOrders)
        
        if totalPaginas is not None:
            return totalPaginas
        else:
            return
    
    @staticmethod
    def getPedidos(token: str, createdAfter: str=None, createdBefore: str=None, marketplaceId: int=None, offset: int=0, marketplace: str=None, status: str=None, days: int=7):
        listOrders = {
            'orders': []
        }
        pedido_instance = Pedido()
        params = {}
        
        params['Content-type'] = 'application/json'
        params['limit'] = '100'
        params['offset'] = f'{offset}'
        
        # Verificando componentes do params
        if marketplaceId is not None:
            params['marketplaceId'] = marketplaceId
            
        if marketplace is not None:
            params['marketplace'] = marketplace
            
        if status is not None:
            params['status'] = status
        
        # Verificando data inicial
        dataAtual = datetime.now().replace(hour=0, minute=0, second=0)
        fusoHorario = timezone(timedelta(hours=-23, minutes=-59))
        if createdAfter is not None:
            createdAfter = datetime.strptime(createdAfter, '%Y/%m/%d')
        else: 
            createdAfter = datetime.now()
            
        if createdBefore is not None:
            createdBefore = datetime.strptime(createdBefore, '%Y/%m/%d')
        else: 
            createdBefore = dataAtual - timedelta(days=7)
        
        # Iniciando dentro do loop de 7 dias
        for i in range(1, days):
            createdAfter = dataAtual - timedelta(i)
            createdBefore = dataAtual - timedelta(i - 1)
            fusoHorario = timezone(timedelta(hours=-23, minutes=-59))

            # Formatar as datas conforme o padrão desejado
            createdAfterFormatted = createdAfter.replace(tzinfo=fusoHorario).strftime('%Y-%m-%dT00:00:00')
            createdBeforeFormatted = createdBefore.replace(tzinfo=fusoHorario).strftime('%Y-%m-%dT23:59:59')
        
            params['createdAfter'] = createdAfterFormatted
            params['createdBefore'] = createdBeforeFormatted
            
            
            totalPaginas = pedido_instance._requisicao(token, params, listOrders)
            
            if totalPaginas > 1:
                # Verificando se possui mais páginas
                for _ in range(totalPaginas):
                    print(f'offset atual: {offset}')
                    offset += 100
                    params['offset'] = f'offset'
                    pedido_instance._requisicao(token, params, listOrders)
        
        return listOrders
    
    @staticmethod
    def getPedido(token: str, idOrder: int):
        data = {}
        endpoint = f'https://api.anymarket.com.br/v2/orders/{idOrder}'
        
        response = httpx.get(endpoint, headers={f'gumgaToken': token})
        
        if response.status_code == 200: 
            data = {
                    'content': json.loads(response.text)
                }
        else:
            if response.status_code == 404: 
                errorMsg = errorAnymarket.throwError('Not Found!', response.status_code)  
                print(errorMsg)  
                data = {
                    'idOrder': idOrder,
                    'content': 'Not Found!'
                }
            else:
                errorMsg = errorAnymarket.throwError(response.text, response.status_code)    
                print(errorMsg)
                data = {
                    'idOrder': idOrder,
                    'content': json.loads(response.text)
                }
         
        return data
    
    @staticmethod 
    def getXmlNfe(token: str, idOrder: int, type: str='sale'):
        data = {}
        endpoint = f'https://api.anymarket.com.br/v2/orders/{idOrder}/nfe/type/{type}'
        
        response = httpx.get(endpoint, headers={f'gumgaToken': token})
        response.encoding = 'utf-8'
        
        if response.status_code == 200: 
            responsedict = json.loads(response.text)
            data = {
                    'type': responsedict['type'],
                    'content': responsedict['url']
                }
        else:
            errorMsg = errorAnymarket.throwError('Not Found!', response.status_code)  
            responsedict = json.loads(response.text)
            print(errorMsg)  
            data = {
                'code': responsedict['code'],
                'content': responsedict['message']
            }
         
        return data
    
    @staticmethod
    def postOrder(token: str, payload: dict= None):
        endpoint ='https://api.anymarket.com.br/v2/orders'
        
        if payload is not None:
            response = httpx.post(endpoint, headers={f'gumgaToken': token}, data=json.dumps(payload))
            
            if response.status_code == 200:
                data = {'order': None}
                responsedict = json.loads(response.text)
                data['order'] = responsedict
                return data
                
            else:
                data = {'error': None}
                responsedict = json.loads(response.text)
                data['error'] = responsedict
                return data
        else:
            return {
                'error': 'Payload is null!'
            }
    
    @staticmethod
    def putOrderPago(token: str, idOrder: int = 0):
        endpoint = f'https://api.anymarket.com.br/v2/orders/{idOrder}(Pago)'
        
        if idOrder > 0:
            payload = {
                "status": "PAID_WAITING_SHIP"
            }
        
            response = httpx.put(endpoint, headers={f'gumgaToken': token}, data=json.dumps(payload))
            if response.status_code == 200:
                data = {'order': None}
                responsedict = json.loads(response.text)
                data['order'] = responsedict
                return data
                
            else:
                data = {'error': None}
                responsedict = json.loads(response.text)
                data['error'] = responsedict
                return data
        else:
            return {
                'error': 'idOrder deve ser diferente de 0!'
            }
    
    @staticmethod
    def putOrderFaturado(token: str, idOrder: int = 0, payload: dict=None):
        endpoint = f'https://api.anymarket.com.br/v2/orders/{idOrder}(Faturado)'
        
        if idOrder > 0 and payload is not None:
            response = httpx.put(endpoint, headers={f'gumgaToken': token}, data=json.dumps(payload))
            if response.status_code == 200:
                data = {'order': None}
                responsedict = json.loads(response.text)
                data['order'] = responsedict
                return data
                
            else:
                data = {'error': None}
                responsedict = json.loads(response.text)
                data['error'] = responsedict
                return data
        else:
            return {
                'error': 'idOrder deve ser diferente de 0 e payload deve conter dados válidos conforme body de requisição descrito no documentação da api!'
            }
            
    @staticmethod
    def putOrderEmTransito(token: str, idOrder: int = 0, payload: dict=None):
        endpoint = f'https://api.anymarket.com.br/v2/orders/{idOrder}(Enviado - Em Transito)'
        
        if idOrder > 0 and payload is not None:
            response = httpx.put(endpoint, headers={f'gumgaToken': token}, data=json.dumps(payload))
            if response.status_code == 200:
                data = {'order': None}
                responsedict = json.loads(response.text)
                data['order'] = responsedict
                return data
                
            else:
                data = {'error': None}
                responsedict = json.loads(response.text)
                data['error'] = responsedict
                return data
        else:
            return {
                'error': 'idOrder deve ser diferente de 0 e payload deve conter dados válidos conforme body de requisição descrito no documentação da api!'
            }
    
    @staticmethod
    def putOrderConcluido(token: str, idOrder: int = 0, payload: dict=None):
        endpoint = f'https://api.anymarket.com.br/v2/orders/{idOrder}(Concluido)'
        
        if idOrder > 0 and payload is not None:
            response = httpx.put(endpoint, headers={f'gumgaToken': token}, data=json.dumps(payload))
            if response.status_code == 200:
                data = {'order': None}
                responsedict = json.loads(response.text)
                data['order'] = responsedict
                return data
                
            else:
                data = {'error': None}
                responsedict = json.loads(response.text)
                data['error'] = responsedict
                return data
        else:
            return {
                'error': 'idOrder deve ser diferente de 0 e payload deve conter dados válidos conforme body de requisição descrito no documentação da api!'
            }    
            
    @staticmethod
    def putOrderCancelado(token: str, idOrder: int = 0, cancelDescription: str=None):
        endpoint = f'https://api.anymarket.com.br/v2/orders/{idOrder}(Cancelado)'
        
        if idOrder > 0 and cancelDescription is not None:
            
            payload = {
                "cancelDetails": cancelDescription,
                "status": "CANCELED"
            }
            
            response = httpx.put(endpoint, headers={f'gumgaToken': token}, data=payload)
            
            if response.status_code == 200:
                data = {'order': None}
                responsedict = json.loads(response.text)
                data['order'] = responsedict
                return data
                
            else:
                data = {'error': None}
                responsedict = json.loads(response.text)
                data['error'] = responsedict
                return data
        else:
            return {
                'error': 'idOrder deve ser diferente de 0 e payload deve conter dados válidos conforme body de requisição descrito no documentação da api!'
            } 
    
    @staticmethod
    def ordersPutEnviaXml(token: str, idOrder: int = 0, xml: str=None):
        endpoint = f'https://api.anymarket.com.br/v2/orders/{idOrder}/nfe'
        
        if idOrder > 0 and xml is not None:
            response = httpx.put(endpoint, headers={f'gumgaToken': token,
                                                    'Content-Type': 'application/xml'}, data=xml)
            
            if response.status_code == 200:
                data = {'order': None}
                responsedict = json.loads(response.text)
                data['order'] = responsedict
                return data
                
            else:
                data = {'error': None}
                responsedict = json.loads(response.text)
                data['error'] = responsedict
                return data
        else:
            return {
                'error': 'idOrder deve ser diferente de 0 e payload deve conter dados válidos conforme body de requisição descrito no documentação da api!'
            } 

    @staticmethod
    def ordersPostfiscalDocument(token: str, idOrder: int = 0, fiscalDocument: str=None):
        endpoint = f'https://api.anymarket.com.br/v2/orders/{idOrder}/fiscalDocument'
        
        if idOrder > 0 and fiscalDocument is not None:
            response = httpx.post(endpoint, headers={f'gumgaToken': token,
                                                    "Content-Type": "multipart/form-data; boundary=---011000010111000001101001"}, data=fiscalDocument)
            
            if response.status_code == 200:
                data = {'order': None}
                responsedict = json.loads(response.text)
                data['order'] = responsedict
                return data
                
            else:
                data = {'error': None}
                responsedict = json.loads(response.text)
                data['error'] = responsedict
                return data
        else:
            return {
                'error': 'idOrder deve ser diferente de 0 e payload deve conter dados válidos conforme body de requisição descrito no documentação da api!'
            } 