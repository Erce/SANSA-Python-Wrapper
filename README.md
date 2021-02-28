# COMPUTER SCIENCE DEPARTMENT, UNIVERSITY OF BONN

* * *

### MA-INF 4314 - Lab Semantic Data Web Technologies - SANSA-Stack Python Wrapper

* * *

[Erce Can Balcioglu](https://github.com/Erce), [Alexander Krasnobaev](https://github.com/AlexMK1991), [Pahulmet Singh](#), [Ulvi Shukurzade](https://github.com/UlviShukurzade)

#### Installation steps:
We installed it by referring to the link below, however, there are some links not working like with java8 and changes in versions of hadoop and spark installed, so we would recommend following this sheet for first time users. A lot of text is straightforward copied from the link below which has been really helpful. 

[https://github.com/SmartDataAnalytics/MA-INF-4223-DBDA-Lab/blob/master/labs/WorkSheet-1.md](https://github.com/SmartDataAnalytics/MA-INF-4223-DBDA-Lab/blob/master/labs/WorkSheet-1.md) 

**We recommend to start with clean ubuntu machine as currently existing packages in your machine can interfere with the project dependencies and can cause errors. It can be dual boot on yout pc or virtual machine on Virtual box.**

* **Virtualbox**: \- it is a virtualization software package similar to VMWare or other virtual tools. We will make use of it to setup and configure our working environment in order to complete assignments.
Here are the steps to be followed:
    -  For a virtual box: https://www.virtualbox.org/wiki/Downloads . Windows host is a 106MB file. Follow the setup instructions.
    - Download the latest Ubuntu ISO from [http://www.ubuntu.com/download/desktop](http://www.ubuntu.com/download/desktop) (use 64 bit).
    - Create a new virtual machine with options: Type = Linux, Version = Ubuntu (64 bit).
    -  Recommended memory size: 4GB
    -  Select: "Create a Virtual Hard Drive Now".
        -  Leave the setting for Hard Drive File Type unchanged (i.e., VDI).
        -  Set the hard drive to be "Dynamically Allocated".
        -  Size: ~15GB
    - The virtual machine is now created.
    - Press “**Start**”
        - Navigate to the Ubuntu ISO that you have downloaded, and Press Start.
        - On the Boot Screen: "Install Ubuntu"
        - Deselect both of "Download Updates while Installing" and "Install Third-Party Software"
        - Press “Continue”
        - If there is option "Install Ubuntu alongside Windows" select that (if you are setting dual boot instead of virtual machine), otherwise, 
        - Select "Erase disk and install Ubuntu"
        - Add your account informations:
        - Name = "yourname"; username = "username"; password = "****"; 
        - **remember these information and machine name as we will need it later**
        - Select "Log In Automatically"
        - Press "Restart Now"


    #
 - ## **Log in to the machine.**
   - Open the terminal (Ctrl + Alt + T) and execute these commands: 
   - Download and upgrade the packages list 
        ```sh
        sudo apt-get update
        sudo apt-get upgrade 
        ```
 - ## **Installing Java 8**
   - Visit the link [https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html ](https://www.oracle.com/java/technologies/javase/javase-jdk8-downloads.html)
   - Or Alternatively to this [link](https://sabahgroups-my.sharepoint.com/:u:/g/personal/shulvi15509_sabah_edu_az/EUCQvQK2UkZMuhV03oJCCJUB62o33zhUBIfel8mz0KYj2g?e=0IwBPT) to download directly without sign-in
   - Download jdk-8u281-linux-x64.tar.gz file. 
   - In the Terminal, enter the following commands: 
    ```sh
    sudo mkdir /usr/lib/jvm
    cd /usr/lib/jvm
    sudo tar xzvf ~/Downloads/jdk-8u281-linux-x64.tar.gz   
    cd jdk1.8.0_281 
    pwd
    ```
    ```sh
    sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk1.8.0_281/bin/java" 0 

    sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk1.8.0_281/bin/javac" 0 

    sudo update-alternatives --set java /usr/lib/jvm/jdk1.8.0_281/bin/java 

    sudo update-alternatives --set javac /usr/lib/jvm/jdk1.8.0_281/bin/javac 

    ```
    ```sh
    update-alternatives --list java 

    update-alternatives --list javac
    ```
    - If everything went right, the following command should give you version of Java without error. 
    ```sh
    java -version
    ```
    - If you entered every command correctly and still there is error, restart might help. Restart and continue from checking version.
       #
    -  Setting environment
    ```sh
    sudo nano /etc/environment 

    #copy and paste the following line at the end of the file
    JAVA_HOME="/usr/lib/jvm/jdk1.8.0_281"
    
    #exit the window by saving changes
    # CTRL+X -> Y ->  *do not change the name* hit enter 
    
    source /etc/environment
    echo $JAVA_HOME 
    ``` 
    **If everythy thing is correct, the line above should give you**

    <pre>/usr/lib/jvm/jdk1.8.0_281</pre> 


    #

 - ## **Installing Maven**
   ```sh
   sudo apt-get update
   sudo apt-get install maven 
   ```

 - ## **Install Hadoop**


   - ### Install  SSH
   ```sh
   sudo apt-get install openssh-server    
   ```
   - ### Configuring SSH 
   ```sh
   ssh-keygen -t rsa -P ""

   #Do not enter file name , hit enter

   cat $HOME/.ssh/id\_rsa.pub >> $HOME/.ssh/authorized\_keys 
   ```


- ## **Installation steps for Hadoop**
        in terminal execute the following commands:
   ```sh
   sudo wget https://downloads.apache.org/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz 

   sudo tar xzf hadoop-3.2.1.tar.gz 

   sudo rm  hadoop-3.2.1.tar.gz 

   sudo mv hadoop-3.2.1 /usr/local 

   sudo ln -sf /usr/local/hadoop-3.2.1/ /usr/local/hadoop 
   
   ```
    - To change ownership of Hadoop to the current user:
    <pre>sudo chown -R $USER /usr/local/hadoop-3.2.1/</pre>

    ```sh
    #Create Hadoop temp directories for Namenode and Datanode  

    sudo mkdir -p /usr/local/hadoop/hadoop_store/hdfs/namenode  

    sudo mkdir -p /usr/local/hadoop/hadoop_store/hdfs/datanode 

    #Again assign ownership of this Hadoop temp folder to current user
    sudo chown -R $USER  /usr/local/hadoop/hadoop_store/

    ```

 - ## **Update Hadoop configuration files**
    ```sh
    #User profile : Update $HOME/.bashrc

    nano ~/.bashrc 
    ```
    ```sh
    #Copy and paste followinglines as ther are to the end of .bashrc file

    #Set Hadoop-related environment variables   

    export HADOOP_PREFIX=/usr/local/hadoop   

    export HADOOP_HOME=/usr/local/hadoop   

    export HADOOP\_MAPRED\_HOME=${HADOOP_HOME}  

    export HADOOP\_COMMON\_HOME=${HADOOP_HOME}  

    export HADOOP\_HDFS\_HOME=${HADOOP_HOME}   

    export YARN_HOME=${HADOOP_HOME}   

    export HADOOP\_CONF\_DIR=${HADOOP_HOME}/etc/hadoop 

 

    #Native path   

    export HADOOP\_COMMON\_LIB\_NATIVE\_DIR=${HADOOP_PREFIX}/lib/native   

    export HADOOP\_OPTS="-Djava.library.path=$HADOOP\_PREFIX/lib/native"  

 

    #Java path   

    export JAVA_HOME="/usr/lib/jvm/jdk1.8.0_281"

 

    #Add Hadoop bin/ directory to PATH   

    export PATH=$PATH:$HADOOP\_HOME/bin:$JAVA\_PATH/bin:$HADOOP_HOME/sbin 
    ```
    **save and exit, do not change anything while exit : CTRL+X -> Y -> *do not change the name* hit enter**
    ```sh
    #In order to have the new environment variables in place, reload .bashrc 
    source ~/.bashrc 
    ```
 - ## **Configure Hadoop**
   ```sh
   cd /usr/local/hadoop/etc/hadoop 
   sudo nano yarn-site.xml 
   ```
    ```sh
    <configuration>  
        <property>  
        <name>yarn.nodemanager.aux-services</name>  
        <value>mapreduce_shuffle</value>  
        </property>  
    </configuration>
    ```
    #
    ```sh
    nano core-site.xml
    ```

    ```sh
    <configuration>  
        <property>
        <name>fs.defaultFS</name> 
        <value>hdfs://localhost:54310</value>  
        </property>  
    </configuration>
    ```
    #
    ```sh
    nano mapred-site.xml
    ```
    ```sh
    <configuration>  
        <property>  
            <name>mapreduce.framework.name</name> 
            <value>yarn</value>  
        </property>
        <property>
            <name>mapred.job.tracker</name>
            <value>localhost:54311</value>
            <description>The host and port that the MapReduce job tracker runs at. If  local", then jobs are run in-process as a single map and reduce task.
            </description>
        </property>  
    </configuration>
    ```
    #
    ```sh
    sudo nano hdfs-site.xml 
    ```
    ```sh
    <configuration> 
        <property>
            <name>dfs.replication</name>  
            <value>1</value> 
        </property>  
        <property>  
            <name>dfs.namenode.name.dir</name> 
            <value>file:/usr/local/hadoop/hadoop_store/hdfs/namenode</value>  
        </property>  
        <property>  
            <name>dfs.datanode.data.dir</name>  
            <value>file:/usr/local/hadoop/hadoop_store/hdfs/datanode</value> 
        </property>  
    </configuration>
    ```
   - ### Finally, set to "/usr/lib/jvm/jdk1.8.0_281" the JAVA_HOME variable in /usr/local/hadoop/etc/hadoop/hadoop-env.sh .
    ```sh
    sudo nano hadoop-env.sh 

    #enter this line at the end of file 
    export JAVA_HOME="/usr/lib/jvm/jdk1.8.0_281" 

    #save and exit 
    ```
    -   ### Now :

    ```sh
    nano ~/.bashrc 
    # copy all lines below and paste at the end of file 
    export PATH=$PATH:/usr/local/hadoop/bin/ 

    PATH=$PATH:/usr/local/hadoop/sbin 
    # save and exit    
    ```
    ```sh
    source ~/.bashrc 
    ```

    ```sh
    hdfs namenode -format   

    start-dfs.sh   

    start-yarn.sh 
    ```
    #
 - ## **Create a directory on HDFS.**
   - **replace \<your_username> with your own user name**

    ```sh

    hdfs dfs -mkdir /user   

    #please replace <your_username> with your actual username
    hdfs dfs -mkdir /user/<your_username> 
    ```


 - ## Track/Monitor/Verify 

    ```sh
    jps
    ```
    ### **Now if the jps command does not work, use the following command:**
    ```sh
    nano ~/.bashrc
    ```    
    ```sh
    #copy and paste following lines at the end of file
    export JAVA_HOME="/usr/lib/jvm/jdk1.8.0_281"
    export PATH=$JAVA_HOME/bin:$PATH 

    #save and exit
    ```    
    ```sh
    source ~/.bashrc 
    ```

   **Now, if you try <code>jps</code> again , it should give you similar output to the following example**
    <pre>
    36673 Master
    155697 Jps
    51081 SparkSubmit
    29739 SparkSubmit
    39838 Worker    </pre>

    For ResourceManager – http://localhost:8088 

    For NameNode – http://localhost:50070 
    Finally, to stop the hadoop daemons, simply invoke stop-dfs.sh and stop-yarn.sh commands. 

 - ## Install Spark 

    ```sh
    mkdir $HOME/spark   
    cd $HOME/spark  
    ```

    - Got on this website: [ https://archive.apache.org/dist/spark/spark-3.0.1/](https://archive.apache.org/dist/spark/spark-3.0.1/)
    - Or alternatively go to this [link](https://sabahgroups-my.sharepoint.com/:u:/g/personal/shulvi15509_sabah_edu_az/EdlfzRLwjkhOjcUR_i4IAuwBMLv6gJjyjSTKM8HgOKa24Q?e=FIAcoc) to download right version
    - find this **spark-3.0.1-bin-hadoop3.2.tgz** version and download it 
    - now, go to the terminal and follow instructions
    ```sh
    cd
    cd ~/Downloads
    ls
    # you should see .tgz file in the list
    ```
    Now use following commands
    
    **replace \<your_username> with your own user name**

    ```sh
    #please replace <your_username> with your actual username

    mv spark-3.0.1-bin-hadoop3.2.tgz /home/<your_username>/spark 

    #Move to the folder you created i.e. spark 
    cd $HOME/spark 
    tar xvf spark-3.0.1-bin-hadoop3.2.tgz 

    nano ~/.bashrc   
    ```


    ```sh
    #copy following lines at the end of file

    export SPARK_HOME=$HOME/spark/spark-3.0.1-bin-hadoop3.2/   

    export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin   
    
    #save and exit
    ```


    ```sh
    source ~/.bashrc  
    ```



    ```sh
    start-master.sh
    start-slave.sh <master-spark-URL>
    spark-shell --master <master-spark-URL> 
    ```

    SparkMaster – http://localhost:8080/   
    use this url instead \<master-spark-URL>

    ```sh
    cd
    ```


 - ##  **Installing Scala**

    ```sh
    wget https://downloads.lightbend.com/scala/2.11.11/scala-2.11.11.tgz   

    sudo tar xvf scala-2.11.11.tgz   
    ```
    ```sh
    nano ~/.bashrc
    ```
    ```sh   
    #copy following lines and paste at the end of file
    export SCALA_HOME=$HOME/scala-2.11.11/   

    export PATH=$SCALA_HOME/bin:$PATH   
    ```
    ```sh
    source ~/.bashrc   

    scala -version 
    ```


 - ## **For Setting up Pyspark:** 

    ```sh
    nano ~/.bashrc 
    ```
  
    ```sh
    export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH 

    export PYSPARK_PYTHON=python3 
    ```
    ```sh
    source ~/.bashrc 
    ```

    ```sh
    pyspark     
    ```
    This will call pyspark and expected output is as following:
    <pre><font color="#4E9A06"><b>ulvi@machinename</b></font>:<font color="#3465A4"><b>~/Desktop</b></font>$ pyspark
    Python 3.8.5 (default, Jul 28 2020, 12:59:40) 
    [GCC 9.3.0] on linux
    Type &quot;help&quot;, &quot;copyright&quot;, &quot;credits&quot; or &quot;license&quot; for more information.
    2021-02-22 01:52:21,004 WARN util.Utils: Your hostname, machinename resolves to a loopback address: 127.0.1.1; using 192.168.0.104 instead (on interface wlo1)
    2021-02-22 01:52:21,005 WARN util.Utils: Set SPARK_LOCAL_IP if you need to bind to another address
    2021-02-22 01:52:21,423 WARN util.NativeCodeLoader: Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
    Setting default log level to &quot;WARN&quot;.
    To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
    2021-02-22 01:52:22,815 WARN util.Utils: Service &apos;SparkUI&apos; could not bind on port 4040. Attempting port 4041.
    2021-02-22 01:52:22,816 WARN util.Utils: Service &apos;SparkUI&apos; could not bind on port 4041. Attempting port 4042.
    Welcome to
        ____              __
        / __/__  ___ _____/ /__
        _\ \/ _ \/ _ `/ __/  &apos;_/
    /__ / .__/\_,_/_/ /_/\_\   version 3.0.1
        /_/

    Using Python version 3.8.5 (default, Jul 28 2020 12:59:40)
    SparkSession available as &apos;spark&apos;.
    &gt;&gt;&gt; 

    </pre>
    

    hit CTRL+Z to exit Spark
    #
  - Now, in your main user downloads folder download, ***rdf.nt*** file from the following [link](https://github.com/SANSA-Stack/SANSA-Stack/tree/develop/sansa-rdf/sansa-rdf-spark/src/test/resources) :[ https://github.com/SANSA-Stack/SANSA-Stack/tree/develop/sansa-rdf/sansa-rdf-spark/src/test/resources](https://github.com/SANSA-Stack/SANSA-Stack/tree/develop/sansa-rdf/sansa-rdf-spark/src/test/resources)

  - Now GO to following [link](https://sabahgroups-my.sharepoint.com/:u:/g/personal/shulvi15509_sabah_edu_az/ESWaAzPWnYZHmvm18vm93AcBJBh_ikskf4ykBmCs-v4Y_g?e=sTlo08) and download the .jar file.

  - Now, open terminal:  

    ```sh
    start-master.sh
    start-slave.sh http://localhost:8080/ 
    ```

    (visit http://localhost:8080/ on browser and copy the new link starting with spark://) 
    
    [Example: URL: spark://machinename:7077 ] here, mashinename is the name of the linux machine that I chose when I installed it.

    ```sh
    #please replace <machinename> with your current machine name
    start-slave.sh spark://<machinename>:7077 
    ```
    ```sh
    # Please replace <your_username> with your current user name

    spark-submit --class "net.sansa_stack.rdf.spark.io.NTripleReader" --master local /home/<your_username>/Downloads/SANSA_all_dep_NO_spark.jar triples "/home/<your_username>/Downloads/rdf.nt"  
    ```
    Go on the browser  http://localhost:8080/ . Refresh it and you will find a worker running. 
    #
    - ## Now go to the [git repository](https://github.com/Erce/SANSA-Python-Wrapper) and download the code. Create a folder on Desktop named sansa and extract the code into that new folder.

    #
    - ## Installation of Python, pip, notebook
        Go to the terminal:

    ```sh
    python3 --version 
    ```
    ## Install pip with following command:  
    ```sh
    sudo apt update
    sudo apt install python3-pip
    pip3 --version   
    ```

    
    
    ```sh
    start-master.sh
    #please replace <machinename> with your current machine name
    start-slave.sh spark://<machinename>:7077 
    ```
    
    ```sh
    pip3 install jupyter 

    pip3 install findspark 

    pip3 install py4j 
    ```
    ## Now, it is time to open Notebook file we previously downloaded,
        
    ```sh
    cd ~/Desktop

    #move to the folder where you put pysansa folder and ML_Notebook.ipynb, in our case 'sansa' (We are assuming this is the folder inside which you have the downloaded    pysansa folder)
    cd sansa
    pip3 install -e pysansa

    python3 -m notebook
    ```    
    ## Now you can open the provided notebookfile and run the cells
    
  + To run the RDF layer examples in Jupyter notebook:
    + Go to rdf directory in sansa directory in Jupyter Notebook
    + Click to rdfExampleNotebook.ipynb
    + Go to 'Cell' in the toolbar and click 'Run all'
    + After a few seconds, you can see the results (Printed triples, printed object attributes, size of triples file etc.)
    
  + To run the Query layer examples in Jupyter notebook:
    + Go to query directory in sansa directory in Jupyter Notebook
    + Click to queryExampleNotebook.ipynb
    + Go to 'Cell' in the toolbar and click 'Run all'
    + After a few seconds, you can see the results (Printed triples, printed dataframe which is returned from Query layer with a sparQL query etc.)
    
  + To run the ML layer examples in Jupyter notebook:
    + Go to ml_notebook directory in sansa directory in Jupyter Notebook
    + Click to ML_Notebook.ipynb
    + Go to 'Cell' in the toolbar and click 'Run all'
    + After a few seconds, you can see the output (You can find the output in the same directory in output_folder)
    
    
# How to use the SANSA-Python-Wrapper in a new/different project:
  + Move pysansa folder to your project's directory
  + Go to your project's directory
  + Install pysansa package by running this command -> ***pip3 install -e pysansa***
  + Create a notebook in the same directory with pysansa
  + Now you can use pysansa and its layers by adding this line in the beginning of your notebook -> ***import pysansa***
  + You can find the example usages in our project under ml_notebook, rdf, query directories in the relevant jupyter notebooks
