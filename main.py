# importing two libraries speech recognition and yagmail
import speech_recognition as x
import yagmail

# creating an recognizer insatnce
recognizer = x.Recognizer()


# Microphone is set as a source for recording the audio
with x.Microphone() as source:
    print('Removing background disturbance..')

    # to clear the background details so that script works accurately to record the audio
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("waiting for your message...")

    recordedaudio = recognizer.listen(source)
    print('Done recording..!')

    # try and except block is used to handle the error, if occured.
try:
    print('Printing the message..')

    # here the recorded audio will be converted in to text form
    text = recognizer.recognize_google(recordedaudio, language='en-US')

    print('Your message:{}'.format(text))

except Exception as er:
    print(er)


message = text
# automate the mails using SMTP protocol
sender = yagmail.SMTP('mukuldhiman853@gmail.com', "Password1@9823")

# here the text meassge is send to the receivers mail id
sender.send(to= 'dhimanmukul307@gmail.com', subject='Voice Based Email Service', contents=message)
