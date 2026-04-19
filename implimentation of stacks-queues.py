import sys
import os
try:
    from stacksQueues import *
except:
    print("Error importing library")
    sys.exit()

def stacks():
    stack1 = stack()
    while True:
        try: responce = int(input("enter what operation\n"f"{'1 - push':<15} {'2 - pop':<15} {'3 - peek':<15}\n"f"{'4 - size':<15} {'5 - isEmpty':<15} {'6 - isFull':<15} {'7 - Exit':<15}\n"))
        except ValueError: responce = 0
        match responce:
            case 1: stack_push_validation(stack1, input())
            case 2: stack_pop_validation(stack1)
            case 3: clear_terminal(); print(peek_validation(stack1))
            case 4: clear_terminal(); print(stack1.size())
            case 5: clear_terminal(); print(stack1.isEmpty())
            case 6: clear_terminal(); print(stack1.isFull())
            case 7: clear_terminal(); break 
            case _: clear_terminal(); print("invalid input")

def queues():
    print("################\nQUEUES")
    queue1 = queue()
    while True:
        try: responce = int(input("enter what operation\n"f"{'1 - enqueue':<20} {'2 - dequeue':<20} {'3 - peek':<20}\n"f"{'4 - size':<20} {'5 - isEmpty':<20} {'6 - isFull':<20} {'7 - Exit':<20}\n"))
        except ValueError: responce = 0
        match responce:
            case 1: queue_enqueue_validation(queue1, input())
            case 2: queue_dequeue_validation(queue1)
            case 3: clear_terminal(); print(peek_validation(queue1))
            case 4: clear_terminal(); print(queue1.Getsize())
            case 5: clear_terminal(); print(queue1.isEmpty())
            case 6: clear_terminal(); print(queue.isFull())
            case 7: clear_terminal(); clear_terminal(); break
            case _: clear_terminal(); print("invalid input")
             

def circular_queues():
        print("################\nCIRCULAR QUEUES")
        circularQueue1 = circularQueue()
        while True:
            try: responce = int(input("enter what operation\n"f"{'1 - enqueue':<20} {'2 - dequeue':<20} {'3 - peek':<20}\n"f"{'4 - size':<20} {'5 - isEmpty':<20} {'6 - isFull':<20} {'7 - Exit':<20}\n"))
            except ValueError: responce = 0
            match responce:
                case 1: queue_enqueue_validation(circularQueue1, input())
                case 2: queue_dequeue_validation(circularQueue1)
                case 3: clear_terminal(); print(peek_validation(circularQueue1))
                case 4: clear_terminal(); print(circularQueue1.size())
                case 5: clear_terminal(); print(circularQueue1.isEmpty())
                case 6: clear_terminal(); print(circularQueue1.isFull())
                case 7: clear_terminal(); clear_terminal(); break
                case _: clear_terminal(); print("invalid input")

def stack_push_validation(stack, item):
        clear_terminal()
        try: stack.push(item)
        except Exception as e: print("\nFAILED TO PUSH ELEMENT", e)

def stack_pop_validation(stack):
        clear_terminal()
        try: stack.pop()
        except Exception as e: print("\nFAILED TO POP ELEMENT", e)

def queue_enqueue_validation(queue, item):
        clear_terminal()
        try: queue.enqueue(item)
        except Exception as e: print("\nFAILED TO ENQUEUE ELEMENT", e)

def queue_dequeue_validation(queue):
        clear_terminal()
        try: queue.dequeue()
        except Exception as e: print("\nFAILED TO DEQUEUE ELEMENT", e)

def peek_validation(any):
        clear_terminal()
        try: any.peek()
        except Exception as e: print("\nFAILED TO PEEK ELEMENT", e)
        return any.peek()

def clear_terminal():
    #if os.name == 'nt': os.system('cls')
    #else: os.system('clear')
    return None
def run():
     while True:
        try: responce = int(input("enter what data structure\n"f"{'1 - stack':<20} {'2 - queue':<20} {'3 - circular queue':<20} {'4 - quit':<20}\n"))
        except ValueError: responce = 0
        match responce:
            case 1: clear_terminal(); stacks()
            case 2: clear_terminal(); queues()
            case 3: clear_terminal(); circular_queues()
            case 4: clear_terminal(); print("Exiting..."); sys.exit()
            case _: clear_terminal(); print("invalid input")

run()
