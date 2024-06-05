import json
import torch

from .vocab import ablang_vocab

class ABtokenizer:
    """
    Tokenizer for the heavy/light chain of antibodies.
    """
    
    def __init__(self, vocab_dir=None):
        self.set_vocab(vocab_dir)
        
    def __call__(self, sequence_list, mode='encode', pad=False, w_extra_tkns=True, device='cpu'):
        
        if w_extra_tkns:
            sequence_list = [sequence_list] if isinstance(sequence_list[0], str) else sequence_list
        else:
            sequence_list = [sequence_list] if isinstance(sequence_list, str) else sequence_list

        if mode == 'encode': 
            data = [self.encode(seq, w_extra_tkns = w_extra_tkns, device = device) for seq in sequence_list]
            if pad: return torch.nn.utils.rnn.pad_sequence(data, batch_first=True, padding_value=self.pad_token)
            else: return data
        elif mode == 'decode': 
            return [self.decode(tokenized_seq) for tokenized_seq in sequence_list]
        else:
            raise SyntaxError("Given mode doesn't exist. Use either encode or decode.")
    
    def set_vocab(self, vocab_dir):
        
        if vocab_dir:
            with open(vocab_dir, encoding="utf-8") as vocab_handle:
                self.vocab_to_token=json.load(vocab_handle)
        else:
            self.aa_to_token = ablang_vocab
            
        self.token_to_aa = {v: k for k, v in self.aa_to_token.items()}
        self.pad_token = self.aa_to_token['-']
        self.start_token = self.aa_to_token['<']
        self.end_token = self.aa_to_token['>']
        self.sep_token = self.aa_to_token['|']
        self.mask_token = self.aa_to_token['*']
        self.unknown_token = self.aa_to_token['X']
        self.all_special_tokens = [
            self.pad_token,
            self.start_token,
            self.end_token,
            self.sep_token,
            self.mask_token,
            self.unknown_token
        ]
     
    def encode(self, sequence, w_extra_tkns=True, device='cpu'):
        
        if w_extra_tkns:
            heavy, light = sequence
            sequence = f"<{heavy}>|<{light}>".replace("<>","")
        
        tokenized_seq = [self.aa_to_token[resn] for resn in sequence]
        return torch.tensor(tokenized_seq, dtype=torch.long, device=device)
    
    def decode(self, tokenized_seq):
        
        if torch.is_tensor(tokenized_seq): tokenized_seq = tokenized_seq.cpu().numpy()
        
        return ''.join([self.token_to_aa[token] for token in tokenized_seq])
    

    
