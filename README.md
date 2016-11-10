
=======
# OBSIDIAN SEEKER

Obsidian seeker software analize both CVS and excel data files that compilate common characteristics of absidian objects.The software allow the identification of a "sample type"  and based on this associate physical, chemical and geographic location of a particular item of the data. Based on the previous identification it will provide clues to link obsidian artefacts with independent pre-european communities.

## Getting started

### Prerequisities

```
Ubuntu 16.04 LTS :https://www.ubuntu.com/download
This is needed for operating system for personal computers and also runs network servers.


Python 3.5.2: https://www.python.org/downloads/release/python-350/
You need to download to interpreted, object-oriented, high-level programming language with dynamic semantics.

Visual Studio : https://www.visualstudio.com/downloads/
It is used to develop computer programs in linux. It can produce both native code and managed code and essential for testing code.

```

### Installing

1. You have to donwnload the "Luxo736-project-dental".
2. In your terminal , use the comands to open Luxo736-project-dental and find inside the file "Obsidian seeker.ipynb".
3. Use the comands to get into Jupyter Notebook once you are in Obsidian seeker.ipynb.
4. An emergent window will display the whole files contained in Luxo736-project-dental. Please select Luxo736-project-dental.
* if you are more familiar with script another option could be replacying the extension .ipynb by .py. the program will run the software in the same way.( syntaxis may change slighly according to different versions)Hightly recomended for test functions.

### Manipulate data files

5. Start by importing you CSV file.
6. With the function "read_my_file" open the content to verify your data.
7. Your data now is ready to be splitted in rows.
8. Differenciate every single piece of "datarows" with the imput print "cell_values"
9. To measure the quantity of data manipulated type "obs_dict" and press enter.

### Once data is identify.Keywords.

10. Type "help" as Keyword to optain following options:
```
 if userinput == 'help':
                print("List of commands:")
                print("Study Area")
                print("Source specific")
                print("List Column (Type: List)")
                print("List Column names (Type: Keys)")

```
11. Use another keyword "Sample_Type" and press enter.
12. Insert a subcomand  "Input Sample_Type:" and press enter. this will retrieve  associate elements
13. confirm your options  typing Y or N.
14. Follow the same methodology for "Study Area","Source specific" as they are part of the important features.

```
if userinput == "Sample_Type":
                    subcommand = input('Input Sample_Type:')
                    if confirmation == "y":
                        subindexes = []
                        for x in range (0, len(indexes)):
                            if (subcommand == Sample_Types[indexes[x]]):
                                subindexes.append(indexes[x])
                            indexes = []
                            indexes = subindexes
                    if confirmation == "n":
                        indexes = []
                        for x in range(0, len(Sample_Types)):
                            if subcommand == Sample_Types[x]:
                                indexes.append(x)

```
15. To identify groups (labels). You have to type "List " this will retrieve "'Type in the column you wish to list: "
16. Use the subcomands: sample_type, study , area, source_specific, sample_ID,xrd_setting and source to diplay any location associated with the number in the sample list:
 ```
 if userinput == "List":
                    subcommand = input('Type in the column you wish to list: ')
                    subindexes = []
                    indexes = []
                    if (subcommand == "Sample_Type"):
                        for x in range(0, len(Sample_Types)):
                            print(Sample_Types[10])
 
 ```
17. Once you identify the association type " keys" this will give you options to "Exit" or continue the program
18. Any imput equivalent to "0"  will return: "Nothing matches input specifications"
19. A final option will give you the chances to reduce you results . choose y or N.
20. Additional samples regarding to count lines rows and sample type colum is optional with the imput "o_dict"

## Contributions

Dr Fabiana Kubke: Tutor Staff, Faculty of Science, University of Auckland 
Dr Dion O'Neale: Supervisor, Faculty of Science, University of Auckland 
Tanya Gray: Tutor Staff,Faculty of Computer Science, University of Auckland 
Manish Kukreja: Staff, Faculty of Computer Science, University of Auckland 
Callum Chalmers: Postgrad Studdent , Faculty of Science, University of Auckland 

## Versioning

Obsidian seeker use 1.1.0 version  
We use semver (http://semver.org/) . ee the releases for a changelog and versions

## Authors

* **Luis Miguel Escalante** - [Luxo736](https://github.com/Luxo736)

See the list of [contributors](https://github.com/Luxo736/Luxo736-project-dental/graphs/contributors) who participated in this project

## License
The present code is under MIT License. As a permissive license, it puts only very limited restriction on reuse and  modifications holding an excellent license compatibility. 

All original data (raw data) was subtracted from original articles selected by Dion O’Neale and are licensed under Creative Commons license Zero (CC0).Data manipulation is allow by owner permission. To avoid infringing third party rights, you should consult with your legal advisor if you are unsure whether you have all the rights you need to distribute original data. 

Adittional files are licensed under the Attribution-ShareAlike 4.0 International license (CC BY-SA 4.0). You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use. Also If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original. 


## Acknowledgments

* Dr Fabiana Kubke inspiration and consideration.
* Callum Chalmer collaboration and support.
* Ahmet Adam friendship and admiration.
* Tanya Gray motivation and patience
