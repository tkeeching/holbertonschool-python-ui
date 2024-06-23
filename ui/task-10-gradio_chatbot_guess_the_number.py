#!/usr/bin/env python3

import gradio as gr
import random

class GuessNumberChatbot:
    def __init__(self):
        self.state = "welcome"
        self.user_guess_mode = False
        self.bot_guess_mode = False
        self.max_number = 0
        self.secret_number = 0
        self.history = []

    def reset(self):
        self.__init__()

    def handle_submit(self, message, history):
        normalized_message = message.lower()

        print('Before submit...')
        print('message ->', message)
        print('normalized_message ->', normalized_message)
        print('history ->', history)

        positive_responses = ['yes', 'y']
        negative_responses = ['no', 'n']

        match self.state:
            case 'welcome':
                welcome_message = 'Hi, do you want to play Guess the number with me?'
                history.append((message, welcome_message))
                self.state = 'start'

            case 'start':
                if message in positive_responses:
                    history.append((message, 'You or I can guess the number, did you want to be the one guessing?'))
                    self.state = 'choose_gameplay'
                elif message in negative_responses:
                    history.append((message, 'Ok, come back later if you want to play Guess the number with me'))
                    self.reset()
                elif history[len(history) - 1][1] == 'I’m sorry, I didn’t understand that. Do you want to play Guess the number with me, yes or no?':
                    history.append((message, 'I guess we don’t understand each other, bye for now.'))
                    self.reset()
                else:
                    history.append((message, 'I’m sorry, I didn’t understand that. Do you want to play Guess the number with me, yes or no?'))

            case 'choose_gameplay':
                if message in positive_responses:
                    history.append((message, 'Ok you guess the number. What is the maximum number we will guess up to?'))
                    self.user_guess_mode = True
                    self.state = 'user_guesses'
                elif message in negative_responses:
                    history.append((message, 'Ok I will guess. What is the maximum number we will guess up to?'))
                    self.bot_guess_mode = True
                    self.state = 'bot_guesses'
                elif history[len(history) - 1][1] == 'I’m sorry, I didn’t understand that, do you want to be the one guessing, yes or no?':
                    history.append((message, 'I guess we don’t understand each other, bye for now.'))
                    self.reset()
                else:
                    history.append((message, 'I’m sorry, I didn’t understand that, do you want to be the one guessing, yes or no?'))
            
            case 'bot_guesses':
                if self.max_number == 0:
                    if int(message) > 2:
                        self.max_number = int(message)
                        self.secret_number = random.randint(1, self.max_number)
                        history.append((message, 'I guess {}'.format(self.secret_number)))
                    elif history[len(history) - 1][1] == 'I’m sorry I didn’t understand that. Please let me know a round number greater than 2 I should guess up to.':
                        history.append((message, 'I guess we don’t understand each other, bye for now.'))
                        self.reset()
                    else:
                        history.append((message, 'I’m sorry I didn’t understand that. Please let me know a round number greater than 2 I should guess up to.'))
                elif self.max_number > 2:
                    if message in positive_responses:
                        history.append((message, 'Great! Come back later if you want to play again.'))
                        self.reset()
                    elif message in negative_responses:
                        history.append((message, 'Ahh, hopefully I will have better luck next time! Come back later if you want to play again.'))
                        self.reset()
                    elif history[len(history) - 1][1] == 'I’m sorry, I didn’t understand that, did I guess the correct number, yes or no?':
                        history.append((message, 'I guess we don’t understand each other, bye for now.'))
                        self.reset()
                    else:
                        history.append((message, 'I’m sorry, I didn’t understand that, did I guess the correct number, yes or no?'))

            case 'user_guesses':
                if self.max_number == 0:
                    if int(message) > 2:
                        self.max_number = int(message)
                        self.secret_number = random.randint(1, self.max_number)
                        history.append((message, 'Ok great, what is your guess?'))
                    elif history[len(history) - 1][1] == 'I’m sorry I didn’t understand that. Please let me know a round number greater than 2 I should guess up to.':
                        history.append((message, 'I guess we don’t understand each other, bye for now.'))
                        self.reset()
                    else:
                        history.append((message, 'I’m sorry I didn’t understand that. Please let me know a round number greater than 2 I should guess up to.'))
                elif self.max_number > 2:
                    if int(message) == self.secret_number:
                        history.append((message, 'You guessed correct! Come back later if you want to play again.'))
                        self.reset()
                    elif int(message) != self.secret_number:
                        print('type(message) ->', type(message))
                        history.append((message, 'Incorrect, my number was {}. Better luck next time. Come back later if you want to play again.'.format(self.secret_number)))
                        self.reset()
                    elif history[len(history) - 1][1] == 'I’m sorry I didn’t understand that. Please let me know what round number is your guess.':
                        history.append((message, 'I guess we don’t understand each other, bye for now.'))
                        self.reset()
                    else:
                        history.append((message, 'I’m sorry I didn’t understand that. Please let me know what round number is your guess.'))

        print('After submit...')
        print('message ->', message)
        print('normalized_message ->', normalized_message)
        print('history ->', history)
        print('self.state ->', self.state)

        return '', history


with gr.Blocks('Guess the number') as demo:
    gr.Markdown('# Guess the number')
    chatbot = gr.Chatbot()
    message = gr.Textbox()
    gr.ClearButton([message, chatbot], value = 'Reset')

    chatbotInstance = GuessNumberChatbot()
    message.submit(chatbotInstance.handle_submit, [message, chatbot], [message, chatbot])

if __name__ == '__main__':
    demo.launch()