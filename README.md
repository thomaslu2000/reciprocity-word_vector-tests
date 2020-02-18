# reciprocity-word_vector-tests

This is a small scale test for the functionality of word vectorization

The lemma_and_vec_demo.py file demonstrates lemmatization (an alternative to stemming) and the word vectorization.
  Lemmatization is like stemming in that it reduces a word to a base form, but turn it into another word rather than a stem.
  This is more ideal when using word vectors since word vectorization libraries are usually dictionaries keyed on real words
  SIDE NOTE: In linguistics, a word that is a derivation of another word can 
    undergo inflectional morphology (only changing things like tense or count) 
    or derivational morphology (changing more in the meaning or part of speech). 
    Many lemmatizers only change inflectional morphology, which preserves more of the original meaning
  
  The vectorization demo shows how two inflected words are similar. As the theory goes, since these vectors are fairly similar,
  it would be more efficient to avoid lemmatization and stemming at all
  
  IMPORTANT NOTE: THIS FILE NEEDS THE GOOGLE PRETRAINED LIBRARY 'GoogleNews-vectors-negative300.bin' TO BE IN THE FOLDER
  
  
The other test so far is v1.py. It uses a much smaller body of text, but trains the model itself (the text is auto-downloading)
  For this test, some text were run through the text cleaning code and the script runs a simulated small-scale matching between 
  bodies of text.
