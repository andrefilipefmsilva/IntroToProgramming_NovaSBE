The encrypt.py and decrypt.py are the final versions of my project. 
They can be used simply by clicking on them on any computer that has Python installed in PATH.
They can also be used by running a cmd from the directory they're in, and typing <python encrypt.py> and <python decrypt.py>.
As is specified in the algorithms, the file to be encrypted or decrypted and the key should be in the same directory as the scripts.

My algorithms build on the original idea of the Polybius square, that had a 5x5 table of characters and assigned two numbers to encode each character.
In the original Polybius Square, the letter "Q", would have for instance the code "31" - 4th row, 2nd column (numbering starts at 0).

My version is enhanced - it allows to enter a key composed by pretty much any ASCII character (it is not limited to a 5x5 table), 
and it allows the user shuffle the alphabet around so he gets its own unique key, that only he knows. 
This key is necessary for decryption - without it, the message cannot be decrypted.

For examples of what I mean, check the files "key1" and "key2". These should be used as examples to test functionality, but the user can
shuffle the characters around in any way preferred. Adding new characters is possible, but removing existing ones is not recommended.

Both the encrypt.py and decrypt.py scripts ask for a .txt message to be entered, as well as the key.
To test functionality, I include in this final version of the project a short message meant for testing functionality. It is named "testfile".
Jointly with one of the keys (key1 or key2), they provide complete functionality to the algorithms.
Feel free to try different messages and different shuffles of the keys.
When experimenting with the algorithm, it is not necessary to write the file name as "testfile.txt". Simply "testfile" will suffice.

You can also use this README file to test my algorithms. It will not output the exact same as the original file (because I have not included
some of the characters used here in the key), but the decrypted message is still very much readable.