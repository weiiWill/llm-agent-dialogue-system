from routing import RouteRecognizer
from dialogue_state import DialogueStateManager
from similar_session_recall import SimilarSessionRecall
from chat_generator import ChatGenerator
from business_qa import BusinessQAModule
from ticket_handler import TicketHandler
from intent_recognizer import IntentRecognizer
from entity_extractor import EntityExtractor
from context_analyzer import ContextAnalyzer
from dialog_manager import DialogManager
from error_handler import ErrorHandler
from strategy_selector import StrategySelector
from response_generator import ResponseGenerator
from user_profile_manager import UserProfileManager
from logger import Logger

class LLMController:
    def __init__(self):
        self.route_recognizer = RouteRecognizer()
        self.state_manager = DialogueStateManager()
        self.session_recall = SimilarSessionRecall()
        self.chat_generator = ChatGenerator()
        self.business_qa = BusinessQAModule()
        self.ticket_handler = TicketHandler()
        self.intent_recognizer = IntentRecognizer()
        self.entity_extractor = EntityExtractor()
        self.context_analyzer = ContextAnalyzer()
        self.dialog_manager = DialogManager()
        self.error_handler = ErrorHandler()
        self.strategy_selector = StrategySelector()
        self.response_generator = ResponseGenerator()
        self.user_profile_manager = UserProfileManager()
        self.logger = Logger()

    def process_input(self, user_input):
        try:
            intent = self.intent_recognizer.recognize(user_input)
            entities = self.entity_extractor.extract(user_input)
            context = self.context_analyzer.analyze(user_input)
            
            self.state_manager.update({
                'intent': intent,
                'entities': entities,
                'context': context
            })
            
            self.dialog_manager.manage()
            
            if self.error_handler.check_for_errors():
                return self.error_handler.handle()
            
            strategy = self.strategy_selector.select()
            sub_agent_response = self.route_to_sub_agent(intent, entities, strategy)
            self.state_manager.update_state(sub_agent_response)
            
            final_response = self.response_generator.generate(sub_agent_response, strategy)
            
            self.state_manager.update_history(user_input, final_response)
            self.user_profile_manager.update(user_input, final_response)
                    
            return final_response
        except Exception as e:
            self.logger.log_error(e)
            return self.error_handler.handle_unexpected()

    def route_to_sub_agent(self, intent, entities, strategy):
        if intent == "chat":
            return self.chat_generator.generate(entities, strategy)
        elif intent == "business_qa":
            return self.business_qa.answer(entities, strategy)
        elif intent == "ticket":
            return self.ticket_handler.process(entities, strategy)
        else:
            return self.chat_generator.generate(entities, strategy)  # 默认为闲聊