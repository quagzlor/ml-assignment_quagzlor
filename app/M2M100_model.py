from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

#Translation Class
class M2M100Translator:
    def __init__(self, src_lang, target_lang):
        self.src_lang = src_lang
        self.target_lang = target_lang
        
        self.model = M2M100ForConditionalGeneration.from_pretrained('facebook/m2m100_418M')
        self.tokenizer = M2M100Tokenizer.from_pretrained('facebook/m2m100_418M', src_lang=src_lang, tgt_lang=target_lang)


    #Method to translate the text
    def translate(self, target_text):

        self.tokenizer.src_lang = self.src_lang
        self.tokenizer.tgt_lang = self.target_lang
    
        model_inputs = self.tokenizer(target_text, return_tensors="pt")
        generated_tokens = self.model.generate(
            **model_inputs, 
            forced_bos_token_id = self.tokenizer.get_lang_id(self.target_lang),
            max_new_tokens=200
        )
        result = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        
        return result[0]