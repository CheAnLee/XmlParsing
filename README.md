# XmlParsing

To parse xml file and provide some features.</br>
## Feature</br>
### xparser.parsing</br>
Split each line read from xml file, and return in List format.</br>
```
ret:<List> = xparser.parsing(Data:<List>)
```
```
RetVal:<List> = [Layer:<Integer>, Signature:<String>, AttrList:<List>]
```

### xparser.filterBySigAndAttr</br>
Return the information by given valid signature list and valid attribute list.</br>
```
ret:<List> = xparser.filterBySigAndAttr(Data:<List>, SigList:<List>, AttrList:<List>)
```
```
RetVal:<List> = [Layer:<Integer>, Signature:<String>, AttrList:<List>]
```
### xparser.showByLayer</br>
Display each line in xml file with indentation, default tabspace is 4.</br>
```
- [3, 'EntityType', [['Name', 'Chassis'], ['BaseType', 'Resource.v1_0_0.Resource']]]
- [3, 'EntityType', [['Name', 'Chassis'], ['BaseType', 'Chassis.Chassis']]]
   - [4, 'Property', [['Name', 'ChassisType'], ['Type', 'Chassis.v1_0_0.ChassisType']]]
       - [5, 'Annotation', [['EnumMember', 'OData.Permission/Read']]]
   - [4, 'Property', [['Name', 'Manufacturer'], ['Type', 'Edm.String']]]
       - [5, 'Annotation', [['EnumMember', 'OData.Permission/Read']]]
   - [4, 'Property', [['Name', 'Model'], ['Type', 'Edm.String']]]
```
## Example</br>
```
python -O main.py <XML_FILE>
```
*-O: not display debug message*
</br></br>
The first element in return list means which layer it belongs. And it also can be used for grouping.
```
[3, 'EntityType', [['Name', 'Chassis'], ['BaseType', 'Resource.v1_0_0.Resource']]]
[3, 'EntityType', [['Name', 'Chassis'], ['BaseType', 'Chassis.Chassis']]]
[4, 'Property', [['Name', 'ChassisType'], ['Type', 'Chassis.v1_0_0.ChassisType']]]
[5, 'Annotation', [['EnumMember', 'OData.Permission/Read']]]
[4, 'Property', [['Name', 'Manufacturer'], ['Type', 'Edm.String']]]
[5, 'Annotation', [['EnumMember', 'OData.Permission/Read']]]
[4, 'Property', [['Name', 'Model'], ['Type', 'Edm.String']]]
```
