# XmlParsing

To parse xml file and provide some features.</br>
## Feature</br>
### xparser.parsing</br>
Split each line read from xml file, and return in List format.</br>
```
ret:<List> = xparser.parsing(Data:<List>)
```
```
RetVal:<List> = [Layer:<Integer>, [Signature:<String>, AttrList:<List>]]
```

### xparser.filterBySigAndAttr</br>
Return the information by given valid signature list and valid attribute list.</br>
```
ret:<List> = xparser.filterBySigAndAttr(Data:<List>, SigList:<List>, AttrList:<List>)
```
```
RetVal:<List> = [Layer:<Integer>, Signature:<String>, AttrList:<List>]
```
## Example</br>
```
python -O main.py <XML_FILE>
```
*-O: not display debug message*
