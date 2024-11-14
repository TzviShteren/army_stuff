import os
from app.kafka_settings.producer import produce
from dotenv import load_dotenv

load_dotenv(verbose=True)


def check_word_in_list(word, sentences):
    return any(word in sentence.lower() for sentence in sentences)


def move_sentence_with_word_to_front(word, sentences):
    contains_word = lambda sentence: word in sentence.lower()

    matching_sentences = list(filter(contains_word, sentences))
    non_matching_sentences = list(filter(lambda s: not contains_word(s), sentences))

    return matching_sentences + non_matching_sentences


def send_to_consumer_service(messages):
    if check_word_in_list("hostage", messages):
        rearranged_messages = move_sentence_with_word_to_front("hostage", messages)
        produce(
            topic=os.environ['MESSAGES_HOSTAGE_TOPIC'],
            key="hostage",
            value=rearranged_messages
        )

    if check_word_in_list("explosive", messages):
        rearranged_messages = move_sentence_with_word_to_front("explosive", messages)
        produce(
            topic=os.environ['MESSAGES_EXPLOSIVE_TOPIC'],
            key="explos",
            value=rearranged_messages
        )
