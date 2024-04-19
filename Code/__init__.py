from otree.api import *
import random

class C(BaseConstants):
    NAME_IN_URL = 'Inflation_Experiment'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # The following two lists contain the texts used in the survey to ask at first about the share invested in different products. The other list contains the descriptions of the personas used in the second part of the survey.
    texts_share_products = ["Denken Sie an ein Inflationsszenario von <b>1,5 %</b> wie in den Jahren 2018-2020. In diesem Szenario gehen Experten auch für die kommenden Jahre von einer niedrigen Inflation (<b>1,5 %</b>) aus. Wie viel Prozent Ihrer Summe X würden Sie in die folgenden Produkte investieren? Beachten Sie, dass Sie bei Ihrer Auswahl 100% erreichen müssen, um fortfahren zu können.",
                            "Denken Sie an ein Inflationsszenario von <b>8 %</b> wie in den Jahren 2021-2023. In diesem Szenario gehen Experten auch für die kommenden Jahre von einer hohen Inflation (<b>8%</b>) aus. Wie viel Prozent Ihrer Summe X würden Sie in diesem Szenario in die folgenden Produkte investieren? Beachten Sie, dass Sie bei Ihrer Auswahl 100% erreichen müssen, um fortfahren zu können.",
                            "Experten erwarten in diesem Szenario eine Phase höherer Inflation wie in den Jahren 2021-2023. Über die Höhe der Inflation, die sich in diesem Szenario einstellen wird, herrscht <b>große Uneinigkeit</b>. Während einige Experten eine Inflation von bis zu 12 % erwarten, sagen andere eine Inflation von eher 4 % voraus. Wie viel Prozent Ihrer Summe X würden Sie in diesem Szenario in die folgenden Produkte investieren? Beachten Sie, dass Sie bei Ihrer Auswahl 100% erreichen müssen, um fortfahren zu können."]
    texts_Personas = ["Sarah, 46, arbeitet als Kundenbetreuerin. Ihr Einkommen dient ausschließlich dazu, die Hypothek für ihr Haus auf dem Lande abzuzahlen und die grundlegenden Lebenshaltungskosten zu decken, so dass kein Raum für Investitionen oder Ersparnisse bleibt. Sarah besitzt keine Aktien/ Aktienfonds oder Ersparnisse außer einem kleinen Notfallfonds. Wie wirkt sich ein Anstieg der Inflation auf die finanzielle Situation von Sarah aus?",
                    "Mia, 45, ist eine erfolgreiche Marketingmanagerin mit einem festen Einkommen und ohne Schulden, Darlehen oder Hypotheken. Sie führt ein liquides Girokonto und hat in ein diversifiziertes Aktienportfolio investiert, wobei sie einer langfristigen Finanzplanung den Vorzug gibt. Wie wirkt sich ein Anstieg der Inflation auf die finanzielle Situation von Mia aus?",
                    "Peter, 25, Softwareentwickler, bezieht ein regelmäßiges Einkommen und lebt schuldenfrei in einer Mietwohnung in einer Großstadt. Obwohl er Wert auf finanzielle Stabilität legt, hat er keine Ersparnisse und keine Börsenanlagen, sondern etwas Geld auf einem Tagesgeldkonto. Wie wirkt sich ein Anstieg der Inflation auf die finanzielle Situation von Peter aus?",
                    "Eleanor, 65, Lehrerin im Ruhestand, genießt ein Leben in ihrem eigenen Haus auf dem Lande (ohne Hypothek) mit einem liquiden Girokonto und einem breit gefächerten Aktienportfolio. Sie hat keine finanziellen Engpässe. Wie wirkt sich ein Anstieg der Inflation auf die finanzielle Situation von Eleanor aus?",
                    "Emily, 26, arbeitet als Grafikdesignerin und hat mit hohen Hypothekenschulden zu kämpfen, die ihre Möglichkeiten zum Sparen oder Investieren einschränken. Trotz ihres stabilen Einkommens machen es die hohen Lebenshaltungskosten in der Stadt schwierig, Ausgaben und Schuldenrückzahlung unter einen Hut zu bringen. Wie wirkt sich ein Anstieg der Inflation auf die finanzielle Situation von Emily aus?",
                    "David, 45, ein Betriebsleiter, führt ein liquides Girokonto für täglichen Ausgaben und Notfälle und legt Wert auf finanzielle Stabilität und Risikovermeidung. Er hat weder Geld auf einem Tagesgeldkonto noch Börseninvestitionen. Wie wirkt sich ein Anstieg der Inflation auf die finanzielle Situation von David aus?",
                    "Patricia, 72, ist auf Renten- und Sozialversicherungsleistungen (z.B. Wohngeld) angewiesen. Mit etwas Geld auf dem Girokonto, aber ohne Börsenanlagen oder Geld auf einem Tagesgeldkonto ist sie finanziell nicht gut gestellt. Wie wirkt sich ein Anstieg der Inflation auf die finanzielle Situation von Patricia aus?"
    ]
    # variables used during the session are saved in this dictionary
    list_vars_session = {}

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    # to save the Prolific id during the session
    prolific_id = models.StringField(initial=" ")
    # used to display the right description for the inflation texts in the first part of the survey
    progress = models.IntegerField(initial=0)
    # to log whether the privacy statement was accepted by the participant
    privacy = models.BooleanField(initial=False)
    # to log the responses for the 5 different products in terms of own assessment of risk to inflation
    likert_1 = models.IntegerField(label='Statement 1', choices=range(1, 6))
    likert_2 = models.IntegerField(label='Statement 2', choices=range(1, 6))
    likert_3 = models.IntegerField(label='Statement 3', choices=range(1, 6))
    likert_4 = models.IntegerField(label='Statement 4', choices=range(1, 6))
    likert_5 = models.IntegerField(label='Statement 5', choices=range(1, 6))
    # contains the text for the different scenarios where the participant should choose how much to invest
    text_share_products_scenario = models.StringField()
    # to log the responses for the different products during the scenarios
    checking_account_value = models.IntegerField()
    overnight_value = models.IntegerField()
    fixed_deposit_value = models.IntegerField()
    bonds_value = models.IntegerField()
    stocks_value = models.IntegerField()
    # to finally save the values, as the page for the scenarios for the investments is displayed multiple times
    text_checking_account_percentages = models.StringField(initial="")
    text_overnight_percentages = models.StringField(initial="")
    text_fixed_deposit_percentages = models.StringField(initial="")
    text_bonds_percentages = models.StringField(initial="")
    text_stocks_percentages = models.StringField(initial="")

    # variable to display the personal information about the persona
    text_personas_scenario = models.StringField(initial="")
    # variable to log the order of the personas to map the results to the different personas
    order_personas = models.StringField(initial="")
    # variable to log how many personas were already displayed
    progress_personas = models.IntegerField(initial=1)
    # field which is displayed to rate the influence of inflation on the finances of the persona
    personasChoice = models.IntegerField(choices = [
        [1, "Sehr negativ"],
        [2, "Gering negativ"],
        [3, "Neutral"],
        [4, "Gering positiv"],
        [5, "Sehr positiv"],
    ],
    widget=widgets.RadioSelect)
    # variable to log the choices from the participants as the page is displayed multiple times
    text_personas_choices = models.StringField(initial="")
    # variable to log the age of the participant
    age = models.IntegerField(choices=[
        [1, "18 - 24 Jahre"],
        [2, "25 - 34 Jahre"],
        [3, "35 - 44 Jahre"],
        [4, "45 - 54 Jahre"],
        [5, "55 - 64 Jahre"],
        [6, "65 - 74 Jahre"],
        [7, "75 Jahre und älter"],
    ],
    widget=widgets.RadioSelect)
    # variable to log the gender of the participant
    gender = models.IntegerField(choices = [
        [1, "Weiblich"],
        [2, "Männlich"],
        [3, "Divers"],
        [4, "Keine Angabe"],
    ],
    widget=widgets.RadioSelect)
    # variable to log the education of the participant
    education = models.IntegerField(choices = [
        [1, "Hauptschulabschluss/Mittlere Reife"],
        [2, "Abitur oder gleichwertiger Abschluss"],
        [3, "Abgeschlossene Ausbildung"],
        [4, "Studium ohne Abschluss"],
        [5, "Vordiplom"],
        [6, "Bachelor-Abschluss/Diplom"],
        [7, "Weiterführendes Studium/Master-Abschluss"],
        [8, "Promotion/PhD"],
        [9, "Keiner der oben genannten"],
    ],
    widget=widgets.RadioSelect)
    # variable to log the working status of the participant
    work = models.IntegerField(choices = [
        [1, "Vollzeit angestellt"],
        [2, "Vollzeit selbstständig"],
        [3, "Teilzeit angestellt"],
        [4, "Arbeitslos"],
        [5, "Student"],
        [6, "Rentner"],
    ],
    widget=widgets.RadioSelect)
    # variable to log the income of the participant
    income = models.IntegerField(choices = [
    [1, "0 € - 999 €"],
    [2, "1.000 € - 1.999 €"],
    [3, "2.000 € - 2.999 €"],
    [4, "3.000 € - 3.999 €"],
    [5, "4.000 € - 4.999 €"],
    [6, "5.000 € - 5.999 €"],
    [7, "6.000 € - 6.999 €"],
    [8, "7.000 € - 7.999 €"],
    [9, "8.000 € - 8.999 €"],
    [10, "9.000 € - 9.999 €"],
    [11, "10.000 € oder mehr"],
    ],
    widget=widgets.RadioSelect)
    # variable to log the stock market participation of the participant
    stock_market_participate = models.BooleanField(choices=[[True, "Ja"],
                                                           [False, "Nein"],])

# PAGES

class Introduction(Page):
    """Generation of the introductory page
    First text for the scenarios of inflation is loaded
    Shuffle of the order for the personas is done and saved in a variable
    """
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.progress = 1
        player.text_share_products_scenario = C.texts_share_products[player.progress-1]
        C.list_vars_session["list_texts_personas_indices"] = random.sample(range(C.texts_Personas.__len__()), k=C.texts_Personas.__len__())
        player.order_personas = ';'.join(str(i) for i in C.list_vars_session["list_texts_personas_indices"])

class Privacy(Page):
    """
    Privacy statement of the player is logged in variable
    """
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.privacy = True


class risk_products_own(Page):
    """
    Participant assessment of the risk of different products in terms of inflation using a likert scale
    Column and row names are created here and sent to the webpage
    """
    form_model = "player"
    form_fields = ['likert_1', 'likert_2', 'likert_3', 'likert_4', 'likert_5']

    def vars_for_template(self):
        # Custom row names
        row_names = {
            1: 'Tagesgeldkonto',
            2: 'Festgeldkonto',
            3: 'Staatsanleihen',
            4: 'Aktien/Aktienfonds',
            5: 'Immobilie',
        }

        # Custom column names
        column_names = {
            1: 'Sehr negativ',
            2: 'Leicht negativ',
            3: 'Neutral',
            4: 'Leicht positiv',
            5: 'Sehr positiv',
        }

        return {
            'row_names': row_names,
            'column_names': column_names
        }


    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.prolific_id = player.participant.label


class preparing_share_products(Page):
    pass
    

class share_products(Page):
    """
    Page is generated to ask participant for investments in different products for different inflation scenarios (1.5, 8 and uncertainty). Values are taken back and double checked, if 100% are reached.
    Additionally, the new text is load for the next page.
    """
    form_model = 'player'
    form_fields = ['checking_account_value', 'overnight_value', 'fixed_deposit_value', 'bonds_value', 'stocks_value']


    @staticmethod
    def error_message(player: Player, values):
        if values['checking_account_value'] + values['overnight_value'] + values['fixed_deposit_value'] + values['bonds_value'] + values['stocks_value'] > 100:
            string_error = "Es können nicht mehr als 100% investiert werden! Bitte investieren Sie 100% Ihres verfügbaren Einkommens. Nutzen Sie dazu die Slider oder die Eingabefelder."
            return string_error
        elif values['checking_account_value'] + values['overnight_value'] + values['fixed_deposit_value'] + values['bonds_value'] + values['stocks_value'] < 100:
            string_error = "Es können nicht weniger als 100% investiert werden! Bitte investieren Sie 100% Ihres verfügbaren Einkommens. Nutzen Sie dazu die Slider oder die Eingabefelder."
            return string_error
        else:
            player.text_checking_account_percentages += str(values['checking_account_value'])+";"
            player.text_overnight_percentages += str(values['overnight_value'])+";"
            player.text_fixed_deposit_percentages += str(values['fixed_deposit_value'])+";"
            player.text_bonds_percentages += str(values['bonds_value'])+";"
            player.text_stocks_percentages += str(values['stocks_value'])+";"


    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.checking_account_value + player.overnight_value + player.fixed_deposit_value + player.bonds_value + player.stocks_value == 100:
            player.progress+=1
            if player.progress < C.texts_share_products.__len__()+1:
                player.text_share_products_scenario = C.texts_share_products[player.progress-1]
        else:
            print("Wrong Investment")


class preparing_personas(Page):
    """
    Preparation of the first Personas page (loading the respective text based on the shuffled list)
    """
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        player.text_personas_scenario = C.texts_Personas[C.list_vars_session["list_texts_personas_indices"][0]]
        

class Personas(Page):
    """
    Load of the Personas page and double check of the correct choice for the personal assessment
    At the end, load of the new text based on the shuffled list
    """
    form_model = 'player'
    form_fields = ['personasChoice']

    @staticmethod
    def error_message(player: Player, values):
        if values['personasChoice'] >= 1 & values['personasChoice'] <= 5:
            player.text_personas_choices += str(values['personasChoice'])+";"
        else:
            error_message = "Bitte wählen Sie eine der Optionen, bevor Sie fortfahren."
            return error_message
        
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if (player.progress_personas < C.texts_Personas.__len__()):
            player.text_personas_scenario = C.texts_Personas[C.list_vars_session["list_texts_personas_indices"][player.progress_personas]]
            player.progress_personas += 1


class preparing_demographics(Page):
    pass


class Demographics(Page):
    form_model = "player"
    form_fields = ["age", "stock_market_participate", "income", "education", "work", "gender"]

class FinalPage(Page):
    pass

page_sequence = [Introduction, 
                 Privacy,
                 risk_products_own, 
                 preparing_share_products, 
                 share_products, 
                 share_products, 
                 share_products, 
                 preparing_personas,
                 Personas, 
                 Personas,
                 Personas,
                 Personas,
                 Personas,
                 Personas,
                 Personas,
                 preparing_demographics,
                 Demographics, 
                 FinalPage]