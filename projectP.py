import receive_message
import logging
import json
from lcd import LCD_HD44780_I2C

def main():
    """Exercise retrieve_sqs_messages()"""

    # Assign this value before running the program
    sqs_queue_url = 'https://sqs.eu-west-1.amazonaws.com/254478186506/demo-queue.fifo'
    num_messages = 1

    # Set up logging
    logging.basicConfig(level=logging.INFO,
                        format='%(levelname)s: %(asctime)s: %(message)s')

    # Retrieve SQS messages
    msgs = receive_message.retrieve_sqs_messages(sqs_queue_url, num_messages)
    if msgs is not None:
        for msg in msgs:
            logging.info(f'SQS: Message ID: {msg["MessageId"]}, '
                         f'Contents: {msg["Body"]}')

#    msg = '{"DeploymentName": "Backend Deployment","RequestedBy": "Ian","TimeStamp": "2019-09-27T05:30:43.511Z","Component": "Backend","Subcomponent": "Function"}'
    # Parse JSON
    jsondata = json.loads(msg["Body"])
#    jsondata = json.loads(msg)
    # Display message on LCD
    lcd = LCD_HD44780_I2C()
    lcd.message = "Incoming Build:\nWhat:{0}\nWho:{1}\nDate:{2}".format(jsondata["Component"],jsondata["RequestedBy"],jsondata["TimeStamp"])

            # Remove the message from the queue
#            delete_sqs_message(sqs_queue_url, msg['ReceiptHandle'])


if __name__ == '__main__':
    main()

