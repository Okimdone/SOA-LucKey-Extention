## Web Service :

- Application on the net. 

- That they allow you to hook to it generally by API/HTTP.

## RPCs -Remote Procedure Calls-: 

* Two pieces of code (client and server) talk over the network, generally using TCP/IP sockets
  * **Stub Code :** Which gets executed on the client side.
  * **Skeleton Code :**  The actual code that does the work and that gets executed on the server-side/ service-provider-side.
* 

## SOAP 1.2 -Simple Object Access Protocol- : 

* Used to serialize a remote procedure call (RPC) across the network.

*  A lightweight mechanism for exchanging structured and typed information between peers in a decentralized, distributed environment using XML.
* A post HTTP request + SOAP ENVOLOP 
*  XML-based protocol that consists of three parts :
  * An envelope that defines a framework for describing what is in a message and how to process it
  * A set of encoding rules for expressing instances of application-defined datatypes (i.e., how to serialize data structures)
  * A convention for representing remote procedure calls and responses

## WSDL 1.1 :

* WSDL (Web Services Description Language) describes
  * what a web service can do.
  * where it resides.
  * how to invoke it.
* WSDL is usually used with SOAP as a transport protocol, although it can work with other protocols as well



### Example of generating java stub from WSDL

java -cp ".\lib\*" org.apache.axis2.wsdl.WSDL2Java  -uri .\bin\InscriptionEcoleArtifacts.wsdl









## 7lmat : 

Work steps to create a structure

1. Formulate the title of the main topic, main target or core message of the Technical Report in one sentence. 
2. Subdivision into 3–4 main items (4-point-structure).
3. Further subdivision into 8–10 main items (10-point-structure). 
4. Further subdivision of extensive main items. 
5. Further subdivision into the ﬁnal detailed structure parallel with the further elaboration of the Technical Report. 
6. Last but not least: Check whether the document part numbers and headings are identical in the structure and in the text (check for completeness and correctness) and add page numbers to the structure to make it a table of contents, if the table of contents shall not be automatically created by your word processor.



## Applied 7lma  :



1. Title of the report : 
   
* DEVELOPMENT AND DESIGN OF SERVICES THAT HELP IMPROVE YOUR ONLINE SHOPPING EXPERIENCE USING SOA Architecture.
   
2. Subdivision into 3–4 main items : 
   * Definition of the Limitations of the actual Shopping experience and the proposed solution.
   * "SOA Principles of Service Design"
   * Using SOA Principles to design the web services
   * Implementation in a way that makes it useful
   
3.  subdivision into 8–10 main items :

   * Definition of the Limitations of the actual Shopping experience and the proposed solution.
     * Abstract
     * Introduction to the problem 
     * Definition of the Solution 
   * "SOA Principles of Service Design" / Case Study
     * Actors
     * Services
     * Business Rules
   * Using SOA Principles to design the web services
     * Modelisation BPMN
     * Orchestration : BPEL
   * Implementation in a way that makes it useful
     * Extraction of the wsdls
     * Generation of the Stub Code Using axis
     * Docker to create a deplyement container
     * AWS to Deploy the services inside the docker container
     * The making of a browser extention **-LucKey-**
     * Apache CXF to generate **JS client code**
     * Testing phase
   * Conclusion and outlook
     * Cool slogen - cool Ext : The "LucKey" extension, u find it, and we get you the best deal.

   

a coupons aggregator and applier service that can be used as a browser extension,

​	it also offers a service that can save ur banking credentials and make a transaction that buys you the wanted item either on a specified date and time or  when its price can get bellow a threshold.

 

1. The Design and Implimentation of an Extention that 





















