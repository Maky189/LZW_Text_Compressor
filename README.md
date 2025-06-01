# LZW (Lempel–Ziv–Welch) Compression algorithm
---

## What is the Lempel-Ziv-Welch algorithm?

A sua invencão deveu-se a Jacob Ziv e Abraham Lempel (J. Ziv and A. Lempel, A universal algorithm for sequential data compression, IEEE Trans. on Information Theory, 1977, 23, pp. 337-343), em ﬁnais dos anos 70: LZ77 e LZ78. Desde então, muitas variantes foram propostas: LZH, LZSS, LZW (Lempel, Ziv, Welch). Este último método deve-se a Terry Welch que em 1984 publicou um artigo onde alguns dos problemas associados `a compressão LZ78 foram eliminados.
Este é o algoritmo de compressão sem perdas mais utilizado. Pode ser usado para comprimir texto, código binário, código executável, imagens (GIF, TIFF, PostScript).

The LZW algorithm is common compression technique that is typically used in GIF and optionally in PDF or TIFF files.

It was invented by Jacob Ziv and Abraham Lempel in the 70s. It has a lot of variants like LZH or LZSS.
The final version was made by Terry Welch wich in 1984 published a article solving some problems related to the algorithm.

It is lossless, meaning no data is lost when compressing. 
The algorithm is simple to implement and has the potential for very high throughput in hardware implementations. It is the algorithm of the widely used Unix file compression utility compress and is used in the GIF image format.

The Idea relies on reoccurring patterns to save data space. LZW is the foremost technique for general-purpose data compression due to its simplicity and versatility. It is the basis of many PC utilities that claim to “double the capacity of your hard drive”.

## How it works?

LZW compression works by reading a sequence of symbols, grouping the symbols into strings, and converting the strings into codes. Because the codes take up less space than the strings they replace, we get compression. Characteristic features of LZW includes, 

LZW compression uses a code table, with 4096 as a common choice for the number of table entries. Codes 0-255 in the code table are always assigned to represent single bytes from the input file.
When encoding begins the code table contains only the first 256 entries, with the remainder of the table being blanks. Compression is achieved by using codes 256 through 4095 to represent sequences of bytes.
As the encoding continues, LZW identifies repeated sequences in the data and adds them to the code table.
Decoding is achieved by taking each code from the compressed file and translating it through the code table to find what character or characters it represents.

Example: ASCII code. Typically, every character is stored with 8 binary bits, allowing up to 256 unique symbols for the data. This algorithm tries to extend the library to 9 to 12 bits per character. The new unique symbols are made up of combinations of symbols that occurred previously in the string. It does not always compress well, especially with short, diverse strings. But is good for compressing redundant data, and does not have to save the new dictionary with the data: this method can both compress and uncompress data. 
There are excellent article's written up already, you can look more in-depth here, and also Mark Nelson's article is commendable. 

## Implementation

The idea of the compression algorithm is the following: as the input data is being processed, a dictionary keeps a correspondence between the longest encountered words and a list of code values. The words are replaced by their corresponding codes and so the input file is compressed. Therefore, the efficiency of the algorithm increases as the number of long, repetitive words in the input data increases.
However in this project we used our own aproach to the algorithm given a version of the algorithm provided by our teacher in the Multimedia class of my University

### To encode:
    1. Inicializa uma sequência (S) a vazio; 
    2. Lê símbolo (x) da mensagem a codiﬁcar; 
    3. Se símbolo é o EOF vai para ponto 7. 
    4. Gera sequência (Sx) da concatenação de S com x (Sx = S+x); 
    5. Se Sx puder ser encontrada no dicionário: 
        (a) S = SX; 
        (b) vai para ponto 2. 
    6. Se Sx não puder ser encontrada no dicionário: 
        (a) é emitido o código de S; 
        (b) Sx é colocada no dicionário; 
        (c) e S é inicializada com o símbolo x. 
        (d) Vai para ponto 2; 
    7. é emitido o código de S;

```python
def encode(sequence: str) -> str:
    #Begin empty sequence
    result = ""
    counter = 1

    for char in sequence:
        if char not in dictionary:
            dictionary[char] = counter
            counter += 1


    # Read a symbol (x) from the message to encode
    first = sequence[0]
    for char in sequence[1:]:
        # go read the symbol again
        # Generate a sequence (Sx) from the concatenation of S with x (Sx = S + x)
        Sx = first + char
        # If Sx can be found in the dictionary:
        if Sx in dictionary:
            # S = SX
            first += char
        else:
            # Omit the encoding of S;
            result += str(dictionary[first])
            # Sx is put in the dictionary
            dictionary[Sx] = counter
            counter += 1
            # and S is made with the symbol of x
            first = char



    # If is the end of the message then go to the end line
    return result + str(dictionary[first])
```

### To decode
    
    1. Initialize the table with sigle character strings
    2. Revert the already created dictionary
    3. Then go through each of the encoded characters and convert them back to the corresponding characters

```python
def decode(sequence: str) -> str:
    codes = [int(i) for i in sequence]
    #Initialize table with single character strings
    result = ""

    #Inverted the old dictionary
    inverted = {v: k for k, v in dictionary.items()}

    #Go thrught all the code and conevert them back to text
    for each in codes:
        result += inverted[each]

    return result
```






