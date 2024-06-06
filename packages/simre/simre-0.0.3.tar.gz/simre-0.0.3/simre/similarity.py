# -*- coding: utf-8 -*-

import nltk
nltk.download('stopwords')
nltk.download('punkt')

import pandas as pd
import string
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer,PorterStemmer
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer, util
import fasttext
import spacy
import os
import csv
from io import StringIO
from statistics import mean
from .formats import get_req_feature

################################## se cargan los modelos pre entrenados #################################
#########################################################################################################

BASE_DIR = os.getcwd()
FILES_DIR = os.path.abspath(os.path.join(BASE_DIR, './fileserver'))

print('Models in path:'+FILES_DIR)

nlp_spacy = spacy.load('es_core_news_sm') 
nlp_spacy_en = spacy.load("en_core_web_sm")

ft = fasttext.load_model(FILES_DIR + '/' + 'cc.es.300.bin') 
ft_en = fasttext.load_model(FILES_DIR + '/' + 'cc.en.300.bin')
                     
model_word2vec = KeyedVectors.load_word2vec_format(FILES_DIR + '/' + 'SBW-vectors-300-min5.bin.gz', binary=True)
w2v_vocab = set(model_word2vec.index_to_key )

model_word2vec_en = KeyedVectors.load_word2vec_format(FILES_DIR + '/' + 'GoogleNews-vectors-negative300.bin.gz', binary=True)
w2v_vocab_en = set(model_word2vec_en.index_to_key )

lista_modelos = [
    ('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2','Multilingual MiniLM-L12-v2'),
    ('sentence-transformers/distiluse-base-multilingual-cased-v2','Multilingual distiluse-cased-v2'),
    ('sentence-transformers/paraphrase-multilingual-mpnet-base-v2','Multilingual mpnet-base-v2')  
                 ]

def load_models():
    
    lista_modelos_ = []    
    for (i,j) in lista_modelos:
        model_multilingual = SentenceTransformer(i)
        lista_modelos_.append(model_multilingual)      
    return lista_modelos_
    
#########################################################################################################
#########################################################################################################

def similarity_process(nameReq,nameFeat,nameDesc,lang,lista_modelos_=[],listModelos_final=[1],threshold=0.7,preprocess=True):
    
    if len(lista_modelos_)<1:
        lista_modelos_ = load_models()
    fileRequirement = open(nameReq, "r")   
    lista_file = []
    file = fileRequirement.read()
    csv_data = csv.reader(StringIO(file), delimiter='\t')        
    lista_file.extend(row[0] for row in csv_data)
    df = pd.DataFrame(lista_file, columns=['New Requirement'])
    df.insert(0, 'ID', range(1, len(df) + 1))
    df_repo = get_req_feature(nameFeat, nameDesc)    

    get_similar_varios(df, df_repo, listModelos_final, lang, lista_modelos_,float(threshold), preprocess)  

def get_nlp_spacy(lang):
    if lang=='es':
        return nlp_spacy
    elif lang=='en':
        return nlp_spacy_en 
    
def get_vocab(lang):
    if lang=='es':
        return w2v_vocab
    elif lang=='en':
        return w2v_vocab_en 
    
def get_model_word2vec(lang):
    if lang=='es':
        return model_word2vec
    elif lang=='en':
        return model_word2vec_en 

def get_fastText(lang):
    if lang=='es':
        return ft
    elif lang=='en':
        return ft_en 

def get_stemmer(lang):
    if lang=='es':
        return SnowballStemmer('spanish')
    elif lang=='en':
        return PorterStemmer 
    
def get_stopwords(lang):
    if lang=='es':
        stopwords_spanish = stopwords.words('spanish')
        stopwords_spanish.extend(['----','---','--',':',',','!','/','.','?','"','>'])
        stopwords_spanish.extend(['…','(',')','“','”',"''",'``','•',';'])
        return stopwords_spanish
    elif lang=='en':
        stopwords_en = stopwords.words('english')
        return stopwords_en 
    
def word_tokenize_with_spacy(texto,lang,vocab=[],stemmer=0):
    """Tokeniza un texto usando spacy (soporta español e inglés)
    Parámetros:
        texto -- texto a procesar
    Salida:
        Un arreglo con las palabras tokenizadas 
    """
    nlp = get_nlp_spacy(lang)
    stopwords = get_stopwords(lang)
    stemmer_ = get_stemmer(lang)
    doc = nlp(texto)
    texto_tokenizado = []    
    for token in doc:
        if len(vocab)==0:
            if token.text.lower() not in stopwords and token.text not in string.punctuation:
                texto_tokenizado.append(token.text.lower()) if stemmer==0 else texto_tokenizado.append(stemmer_.stem(token.text.lower()))
        else:
            if token.text.lower() not in stopwords and token.text not in string.punctuation and token.text.lower() in vocab:
                texto_tokenizado.append(token.text.lower()) if stemmer==0 else texto_tokenizado.append(stemmer_.stem(token.text.lower()))
    return texto_tokenizado

def genera_archivo_txt(df,nombre):
    """Genera un archivo de extensión csv.
    Parámetros:
        lista -- array con los datos
        nombre -- nombre que tendrá el archivo
    Salida:
        Se creará un archivo en la misma carpeta donde se encuentra este 
        archivo con el nombre indicado más la fecha actual.
    """
    nombreArchivo = nombre + ".csv"
    df.to_csv(nombreArchivo, encoding='utf-8',index=False)
   
def prediccion_fastText(texto, modelo):
    prediccion_modelo = modelo.predict(texto)
    label_pred = prediccion_modelo[0][0]
    retorna = ''
    retorna = label_pred[9:]
    return retorna

def get_similarity_fasttext(sentence,sentence_,lang,preprocess, stem):
    """Obtiene el similarity score entre dos oraciones usando los word embeddings proporcionados por fastText
    Parámetros:
        sentence, sentence_ -- requisitos a comparar la similitud
        lang -- idioma ('es','en')
        preprocess -- indica si se realizará un preprocesamiento
    Salida:
        Similarity score
    """
    if preprocess:
          sentence = ' '.join([i for i in word_tokenize_with_spacy(sentence,lang,[],stem)])
          sentence_ = ' '.join([i for i in word_tokenize_with_spacy(sentence_,lang,[],stem)])
    if (len(sentence) == 0) or (len(sentence_) == 0) or (sentence.strip() == "") or (sentence_.strip() == ""):
          return
    else:
        ft = get_fastText(lang)
        sentence1 = ft.get_sentence_vector(sentence)
        sentence2 = ft.get_sentence_vector(sentence_)     
        sim = cosine_similarity([sentence1],[sentence2])  
    return ('fastText',float(sim[0][0]))

def get_similarity_transf(sentence1,sentence2,modelos,lang,preprocess, stem,lista_modelos_):
    """Obtiene el similarity score entre dos oraciones usando modelos pre entrenados (sentence transformers)
    Parámetros:
        sentence, sentence2 -- requisitos a comparar la similitud
        modelos -- 1,2,3
        lang -- idioma ('es','en')
        preprocess -- indica si se realizará un preprocesamiento
    Salida:
        Similarity score
    """
    lista_final = []
    if (len(sentence1) == 0) or (len(sentence2) == 0) or (sentence1.strip() == "") or (sentence2.strip() == ""):
        return lista_final
    else:
        if preprocess:
            sentence1 = ' '.join([i for i in word_tokenize_with_spacy(sentence1,lang, [],stem)])
            sentence2 = ' '.join([i for i in word_tokenize_with_spacy(sentence2,lang, [],stem)])
        
        for i,model in enumerate(lista_modelos_):
            if i+1 in modelos:
                embeddings = model.encode([sentence1, sentence2])
                similarity_score = util.pytorch_cos_sim(embeddings[0], embeddings[1]).item()
                lista_final.append((lista_modelos[i][1],similarity_score))  
            else:
                continue           
    return lista_final

def get_similarity_word2vec(sentence1,sentence2,lang,stem):
    """Obtiene el similarity score entre dos oraciones usando los word embeddings proporcionados por fastText
    Parámetros:
        sentence, sentence_ -- requisitos a comparar la similitud
        lang -- idioma ('es','en')
        preprocess -- indica si se realizará un preprocesamiento
    Salida:
        Similarity score
    """
    w2v_vocab = get_vocab(lang)
    model = get_model_word2vec(lang)
    sentence = [model.get_vector(i) for i in word_tokenize_with_spacy(sentence1,lang,w2v_vocab,stem)]
    sentence_ = [model.get_vector(i) for i in word_tokenize_with_spacy(sentence2,lang,w2v_vocab,stem)]
       
    if (len(sentence) == 0) or (len(sentence_) == 0):
          return 0
    else:      
       sim = model.n_similarity(sentence, sentence_)
    return ('word2vec',float(sim))

    
def get_similar_varios(df, df2, modelos,lang,lista_modelos_,threshold=0.7, preprocess = True):
    """Realiza el proceso de similitud
    Parámetros:
        df -- dataframe con el listado de los requisitos
        df2 -- dataframe con los requisitos a comparar
        lang -- idioma 'es','en'
    Salida:
        dataframe con los datos
    """
    stem = 0
    df_list = pd.DataFrame()
    for _, row in df.iterrows(): 
        
        new_row={}
        lista_final = []        
        if 'ID' in df.columns:
            new_row['ID'] = row['ID']    
        sentence = row['New Requirement']
        new_row['New Requirements'] = sentence            
                
        for _, row2 in df2.iterrows(): 
            
            sentence_target = row2['descripcion']   
            lista_final = []   
            if sentence_target is None or not isinstance(sentence_target, str) or sentence_target == '':
                continue
            if 1 in modelos or 2 in modelos or 3 in modelos:
                lista_final = get_similarity_transf(sentence,sentence_target,modelos,lang,preprocess,stem,lista_modelos_)
            if 4 in modelos:
                sim = get_similarity_word2vec(sentence,sentence_target,lang,stem)
                if sim !=0:
                    lista_final.append(sim)
            if 5 in modelos:
                sim2 = get_similarity_fasttext(sentence,sentence_target,lang,preprocess,stem)
                lista_final.append(sim2)
                
            lista_scores = [tupla[1] for tupla in lista_final]
            if len(lista_scores)>0:
                if mean(lista_scores) > threshold:
                    new_row['Average Similarity'] = [round(mean(lista_scores),3)]                 
                    new_row['Similar Requirement'] = [sentence_target]
                    if 'name' in df2.columns:
                        name = row2['name'] 
                        new_row['Feature'] = [name]                         
                    
                    if 'mandatory' in df2.columns:
                        obl = row2['mandatory']
                        if obl not in [None, '']:
                           obl = str(obl)
                        else:
                            obl = 'False'
                        new_row['Mandatory'] = [obl]  
                    
                    for tupla in lista_final:
                        new_row['Similarity ' + tupla[0]] = [round(tupla[1],3)]  
                   
                    df_2 = pd.DataFrame(new_row)
                    df_list = pd.concat([df_list, df_2], ignore_index = True)
                
    if df_list is not None and not df_list.empty:
        genera_archivo_txt(df_list,'Similarity List')  
    return df_list
     