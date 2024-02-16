import streamlit as st
import json
from datetime import datetime, timedelta
import random

def render_algoritmo():
    st.title('Decoreba - Revisão de Flashcards')
    st.subheader('Selecione a especialidade e o tópico para revisão:')
    
# Classe Flashcard
class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.next_review = datetime.now()

    def review(self, correct):
        if correct:
            self.next_review += timedelta(days=3)
            self.next_review_2 = self.next_review + timedelta(days=3)
            self.next_review_3 = self.next_review_2 + timedelta(days=3)
        else:
            self.next_review += timedelta(hours=12)

# Classe FlashcardDeck
class FlashcardDeck:
    def __init__(self):
        self.decks = {}

    def add_flashcard(self, subject, topic, flashcard):
        if subject not in self.decks:
            self.decks[subject] = {}
        if topic not in self.decks[subject]:
            self.decks[subject][topic] = []
        self.decks[subject][topic].append(flashcard)

    def load_flashcards_from_json(self, file_path, subject):
        with open(file_path, 'r') as file:
            flashcards_data = json.load(file)
            for topic, cards in flashcards_data.items():
                for card_data in cards:
                    flashcard = Flashcard(card_data['question'], card_data['answer'])
                    self.add_flashcard(subject, topic, flashcard)

    def review_flashcards(self, subject, topic):
        if subject not in self.decks or topic not in self.decks[subject] or not self.decks[subject][topic]:
            st.error(f"Nenhum flashcard disponível para revisão no assunto '{topic}' da especialidade '{subject}'.")
            return

        while True:
            current_time = datetime.now()
            due_flashcards = [flashcard for flashcard in self.decks[subject][topic] if flashcard.next_review <= current_time]

            if not due_flashcards:
                st.success(f"Todos os flashcards no assunto '{topic}' da especialidade '{subject}' estão atualizados. Nenhum flashcard para revisão neste momento.")
                return

            random_flashcard = random.choice(due_flashcards)
            st.write("Pergunta:", random_flashcard.question)
            st.text_input("Responda e pressione Enter para ver a resposta: ")
            st.write("Resposta:", random_flashcard.answer)
            correct = st.selectbox("Você acertou?", ("Sim", "Não")) == "Sim"
            random_flashcard.review(correct)
            if correct:
                st.success("Flashcard revisado. Próximas revisões agendadas para:")
                st.write("3 dias após a resposta correta:", random_flashcard.next_review)
                st.write("6 dias após a resposta correta:", random_flashcard.next_review_2)
                st.write("9 dias após a resposta correta:", random_flashcard.next_review_3)
            else:
                st.error("Você errou. Este flashcard será revisado novamente em 12 horas.")
                st.write("Próxima revisão agendada para:", random_flashcard.next_review)
            st.write("\n--- Próximo flashcard ---\n")

# Função principal
def main():
    st.title('Decoreba - Revisão de Flashcards')
    st.subheader('Selecione a especialidade e o tópico para revisão:')

    deck_manager = FlashcardDeck()

    # Carregar flashcards de Psiquiatria do arquivo JSON local
    file_path_psiquiatria = r'D:\Decoreba\data\flashcards\flashcards_psiquiatria.json'
    deck_manager.load_flashcards_from_json(file_path_psiquiatria, "Psiquiatria")

    # Carregar flashcards de Urgência e Emergência do arquivo JSON local
    file_path_urgencia_emergencia = r'D:\Decoreba\data\flashcards\flashcards_urgencia_e_emergencia.json'
    deck_manager.load_flashcards_from_json(file_path_urgencia_emergencia, "Urgência e Emergência")

    # Obter especialidade escolhida
    chosen_specialty = st.selectbox("Especialidade:", ["Psiquiatria", "Urgência e Emergência"])

    # Obter tópico escolhido
    topics = list(deck_manager.decks[chosen_specialty].keys())
    chosen_topic = st.selectbox("Tópico:", topics)

    # Revisão dos flashcards no tema escolhido da especialidade escolhida
    deck_manager.review_flashcards(chosen_specialty, chosen_topic)

# Executar a função principal
if __name__ == '__main__':
    main()
