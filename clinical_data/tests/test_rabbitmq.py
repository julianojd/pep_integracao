import json
from unittest import mock
from app.rabbitmq import publish_message


# Testa se a função publica uma mensagem na fila

@mock.patch('app.rabbitmq.pika.BlockingConnection')
def test_publish_message_success(mock_blocking_connection):
    # Configura o mock para a conexão
    mock_connection = mock.Mock()
    mock_channel = mock.Mock()

    # Simula os métodos da conexão e do canal
    mock_blocking_connection.return_value = mock_connection
    mock_connection.channel.return_value = mock_channel

    # Dados de exemplo
    queue_name = 'test_queue'
    message = {"key": "value"}

    # Chama a função a ser testada
    publish_message(queue_name, message)

    # Verifica se a conexão foi estabelecida
    mock_blocking_connection.assert_called_once()

    # Verifica se o canal foi declarado
    mock_channel.queue_declare.assert_called_once_with(queue=queue_name, durable=True)

    # Verifica se a mensagem foi publicada corretamente
    mock_channel.basic_publish.assert_called_once_with(
        exchange='',
        routing_key=queue_name,
        body=json.dumps(message),
        properties=mock.ANY
    )

    # Verifica se a conexão foi fechada
    mock_connection.close.assert_called_once()
