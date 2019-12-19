README for Query Engine for English Treebank Database
----------------------------------------------------------------------------------------------------------------------------------------
NOTE:
The following files and structure is required for functioning of the code
	Treebank_english.db, query_english.py,E_Createdata.py,E_Modules.py  [Place the files in the same directory]
The last two are required only if you want to view the tree of sentences.
1.Treebank_English.db

	Treebank_English.db contains two tables: Tsentence and Tword. It was extracted from UNIVERSAL DEPENDENCIES' ENGLISH-EWT CONLLU FILES(train,dev,test)
	(i) Tsentence:
			Tsentence contains the following information:
				Sno,sid,words,sentence,filename
	(ii) Tword:
			Tword contains the follow information:
				SNo,sid,word,wid,root,pos_UD,pos_ILMT,Case1,Gender1,Number1,Person1,PronType,VerbForm,Voice,Mood,Tense,NumType,Poss,Foreign1,Definite,Degree,Reflex,Typo,Abbr,parent,rel,SpaceAfter,CopyOf,CheckReln,CheckAttachment,CheckUPOS,filename

2.queries_english.py:
	(i)The above python file is used to generate query and access the database Treebank_English.db(The English Treebank). Open the terminal and type the following command to run the above python file.
			python queries_english.py
			NOTE: PLEASE ENSURE THE DATABASE 'Treebank_Hindi.db' IS PLACED IN THE SAME DIRECTORY AS 'query_english.py'
	(ii) You will get the following options once the python program is run:
		1.No of words in a sentence
		2.No of minor field types and information
		3.POS combinations and respective records
		4.Identify parent(word) corresponding to each word in a given sentence
		5.To find the word and it's gender in a given sentence
		6.To obtain information about a given relation, including corresponding POS's and sentences
		7.To obtain sibling relations in a given sentence
		8.To obtain Noun followed by verb cases and print relation
		9.To print the sentences for single constructs
		10.Double-word Constructs(consecutive).To print the details of these constructs
		11.Double-word Constructs(non-consecutive) and to print the parents and child
		12.To print the tree of a sentence given it's id
		13.To print the tree of all sentences in a file
		14.Quit

		Please select one of the options(1-14)
  (iii) If you had selected:
		OPTION 1 :
	 	This basically gives the no of words in a sentence.

		So just input the Sentence No. for which you want to know the no. of words.You will get the no of words once you input the sentence id.
  	----------------------------------------------------------------------------------
		OPTION 2:
		This query gives all the minor field types of a morphological type that exist in the database, and the words of the database of a certain field type, if needed.

		Initially you have to input one of the following options as input:

		Definite,PronType,Number1,Mood,Person,Tense,VerbForm,NumType,Degree,Case1,Gender1,Poss,Foreign1,Voice,Reflex,Typo,Abbr

		The minor field types will be displayed on the terminal along with the number of occurences.
		Next, Press 'Y' or 'y' if you want to view the words for a particular field type. Else,press any other key.
		If you had pressed 'y' or 'Y', then enter the field type for which you want to view the words.
		The words for the entered type will be stored in the file 'morphdetails_english.txt'(stored in the same directory as your query program file).
		----------------------------------------------------------------------------------
		OPTION 3:
		This option gives the different types of pos_UD and pos_ILMT pairs, and the no of occurrences of each type. Also, one can	choose to view the words of a certain pair of pos_UD and pos_ILMT.

		All the types of pos_UD and pos_ILMT pairs are displayed first, along with the number of occurrences.Press 'Y' or 'y' if you want to view the words belonging to a certain type. Enter the pos_UD and pos_ILMT type, and you can view the words in the file 'UD-ILMT_occurrence_english.txt'(stored in the same directory as your query program file).
		----------------------------------------------------------------------------------
		OPTION 4:
		This gives the parent for every word in a given sentence.

		The user has to input the sentence-id and the word-parent pairs will be stored in a file named 'word-parent_english.txt'(stored in the same directory as your query program file).
		------------------------------------------------------------------------------------
		OPTION 5:
		This gives word and it's gender in a given sentence.

		The user has to input the sentence-id and the word and it's gender will be stored in a file named	'Word-Gender_enflish.txt'(stored in the same directory as your query program file).
		--------------------------------------------------------------------------------------
		OPTION 6:
		This option gives the POS of the child and the parent and the no of occurrences of each type. Also the parent-child pairs for	a case obtained if the user wishes to.

		The user has to input the relation required, and types of POS of child and parent along with no of occurrences is printed in the terminal. Press 'y' or 'Y' if you want to view word by word cases of a given type.Else, press any other key.
		Now, enter the POS of parent and child. All word by word cases of the required type will be in the file 'relation_to_word_mapping_english.txt'(stored in the same directory as your query program file).
		---------------------------------------------------------------------------------------
		OPTION 7:
		This option is to print the parent and the SentenceId for two user input relations of two siblings with their parent.

		All the relations that exist in the document will be displayed in the terminal and the user has to choose any two relations for	which he/she wishes to check sibling relationship. The output will be the filename and the corresponding parent-id in the terminal.
		---------------------------------------------------------------------------------------
		OPTION 8:
		This is to find all cases in which the noun is followed by verb, and the relation that exists between the noun and the verb.

		The file 'noun-verb_english.txt' will contain the noun and the verb(where noun is succeeded by verb) along with the relation that exists between them.
		---------------------------------------------------------------------------------------
		OPTION 9:
		This option is to print the sentences that contain the following single constructs:
		1.although 2.while 3.as 4.because 5.but 6.since 7.unless 8.whether 9.or 10.and

		The user has to input the construct for which he/she wants to view the sentences.(NOTE: DON'T CAPITALIZE ANY OF THE LETTERS THAT YOU ENTER.YOU WILL LOOSE SOME CASES!!!!) The sentences that have the construct you entered will be stored in a file named '<construct-name.txt>'.
		Eg:If you had chosen 'while' construct, then the particulars of the sentences that have 'while' will be stored in 'while.txt'(Similarly for other constructs).
		---------------------------------------------------------------------------------------
		OPTION 10:
		This option is to print the sentences that have double-word constructs(consecutive-case). It includes the following cases:
		1.even-if 2.even-though

		The user has to input the construct(word by word) for which he/she wants to view the sentences.(NOTE: DON'T CAPITALIZE ANY OF THE LETTERS THAT YOU ENTER.YOU WILL LOOSE SOME CASES!!!!). The sentences that have the construct you entered will be stored in a file named '<word1>-<word2>.txt'.
		Eg: If you had chosen 'even-if' construct, then the particulars of the sentences that have 'even' and 'if' will be stored in 'while.txt'(Similarly for other constructs).
		----------------------------------------------------------------------------------------
		OPTION 11:
		This option is to print the sentences that have double-word constructs(non-consecutive-case). It includes the following cases:
		1.either-or2.neither-nor3.since-then

		The user has to input the construct(word by word) for which he/she wants to view the sentences.(NOTE: DON'T CAPITALIZE ANY OF THE LETTERS THAT YOU ENTER.YOU WILL LOOSE SOME CASES!!!!). The sentences that have the construct you entered will be stored in a file named '<word1>-<word2>.txt'.
		Eg: If you had chosen 'even-if' construct, then the particulars of the sentences that have 'even' and 'if' will be stored in 'while.txt'(Similarly for other constructs).
		----------------------------------------------------------------------------------------
		OPTION 12:
		This option is for viewing the tree of a particular sentecne.
		NOTE: PLEASE ENSURE YOU HAVE STORED THE PYTHON FILES E_Createdata.py AND E_Modules.py STORED IN THE SAME DIRECTORY AS query_english.py

		The user has to input the sentence-id for which he/she wants to view the tree. Initially a file with extension '.dat' containing the parsed output of the sentence(in conll format) will be created inside the folder 'conll_single'(present inside folder 'conll').
		The tree is present in the folder 'trees'(present inside 'conll_single').
 		NOTE: In case you don't get the tree for a sentence, please check the log file 'E_log'.
		---------------------------------------------------------------------------------------
		OPTION 13:
		This option is for viewing the trees of all the sentence-ids present in a particular file.
		NOTE: This query works for all files that have the sentence-id in the following format:
			Sentence Id:<sentence-id>
			Eg: Sentence Id:weblog-juancole.com_juancole_20041120060600_ENG_20041120_060600-0003

		The user has to input the name of the file for which he/she wants to view the trees. If the name of the file be <filename>.txt, then:
		User will be given an option to view the tress for 1. First ten sentences 2. All sentences 3. Any particular sentence
		Choose one of the three options.(1, 2 or 3).
		The trees will be in the path conll/conll_<filename>/trees/'filename'.png
		Eg: If the user input is while.txt. Then the trees will be in the path conll/conll_while/trees/
		---------------------------------------------------------------------------------------
		OPTION 14:
		This option is to quit the query search engine.
		---------------------------------------------------------------------------------------

	(iv) You will get an option whether to continue accessing the query engine or not. Press 'Y' or 'y' to continue and 'N' or 'n' to	quit the engine.

	    On pressing 'Y' Or 'y', you will go back to step 1.(ii).
-----------------------------------------------------------------------------------------------------------------------------------------

NOTE FOR THE DEVELOPERS:

1. New Query:
	Add the purpose to the initial print statement that lists all the different queries in the program.
  The new query is basically an addition to the existing
2. All files that contain particulars of a query will be in the same directory as the program. To change the location, alter the path in the file open statements in the program.
3. Purpose of the initial commands:
		conn = sqlite3.connect('Treebank_English.db') - This creates a connection with the database 'Treebank_English.db'
		cursor = conn.cursor() - This creates a cursor that is used to access the database.
		conn.commit()- Any changes to the database will be saved
		conn.close() - The connection with the database will be broken(closed).
