# QuickIE
Framework for building information extraction systems faster, from ground-zero or above.

## Goals and Description

Information Extraction -- systems that build knowledge bases by extracting structured information from unstructured and semi-structured corpora -- are annoyingly slow and expensive to build.  Why?  There are at least three major mutually orthogonal difficulties:

1. Defining the task(s) - what does "important" mean for this system, and what sort of class definitions and structures represent this notion of "importance" necessarily and sufficiently.
2. Collecting training data for the task definitions.  This typically is done via some hybrid of distant supervision, labeling heuristics,  and expert and crowdsourced manual annotation of structures. <!--Cite Old Jurafsky and Ng, Weld, Deepdive and Snorkel, Crowdtruth, Culotta, CASTLE, ... -->
3. Building an accurate, sophisticated extraction pipeline that can leverage the labeled and unlabeled corpora to automatically produce extractions (ie, predicted annotations) which correspond to task definitions, without the need for extensive feature and architecture engineering.

QuickIE aims to address (1) and (2) by uniting this process under a hybrid formalism:

 (1) lambda calculus over implicitly defined knowledge graph schemas - define what questions the KB should be able to answer (queries) and how to answer them (logical compositional statements/algorithms over KG queries)
 
 (2) using the infered schema from (1) to generate microtasks which break up the KG requirements into manageable pieces, then rapidly acquiring annotations using crowd-sourcing.

### Defining Tasks

Defining the information extraction tasks for a specific application is itself a hard question to answer correctly in the absract. It's just plain hard to think about "what are my entities, which interactions are relations or events, do I have a heierarchy, which slots are properties, what is the conditional ordering of my decision process, wait what is my decision process, how will this thing even be used,..."

Instead, we advocate and operational view of defining tasks: **when exploring the collection, what questions do I want answered?**

Under this "assisted-observational" view, we view tasks as being defined by *Questions* that an analyst would ask of another person, who had read the documents or had knowledge of the domain. For these questions to be answerable by a structured KB, they must correspond to logical *Queries* which are specified via some logical composition of actualized subqueries. Initially we consider lambda-DCS [Cite lambda-DCS] as the logical "glue". 

Each *Query* corresponds to a relation (of potentially very high order). Each relation (and equivalently a query) may have an "explanation" which is equivalent to a set of grounded spans to freetext attributes in the KG.

0th order relations are "tagging" functions that find "mentions" (here mention subsumes all sets of grounded tags) in text.  They do not have any child queries.  They are the only relations/queries/functions that **must be grounded**.

All higher order relations contain the result of at least one actualized subquery, and some logical composition of them.  Higher order relations **may also be grounded**, but their grounding is the union of their explicit grounding and the grounding of all actualized subqueries.


#### Example of Exploratory Question-Drilling

- Was there a food poisoning outbreak?
  - := Did more than one food poisoning event occur within one week?
  - ::= size(food poisoning event set) where occurs_within(fp event set, one week) > 1?
    - food poisoning event set := What are the food poisoning events?
    - ::= select (food poisoning events)
      - food poisoning event := Did a person get sick from eating at a restaurant?
      - ::= if Person(p), GotSick(e1), Arg-Object(e1, p) // person got sick
            and Ate(e2), Restaurant(r), Food(f), Arg-Object(e2, p), Arg-Place(e2, r), Arg-Item(e2, f) // and they ate food at restaurant
            and Arg-Eat(e1, e2) // and the eating event is associated with this sick event 
      - Person(p) := Is there a Person in this freetext?
      - GotSick(e1) := Did a Person get sick? --> GotSick conditional on "Person" present
      - Ate(e2) := Did a Person eat? --> Ate conditional on "Person" present
      - Restaurant(r) := Is there a Restaurant mentioned?
      - Food(f) := Is there a food item mentioned?
      - 
      ** Notes: 
      - A conditional statement corresponds to a property filling relation, where the property is conditional on the entity being present.
      Eg, "Did a Person get sick? -> Exists Person where Person.got_sick is defined and true
      - However, if this property may then have relations defined on it, it is hoisted to a conditional event where now Person and the event are related through the e2.Arg-Object.p
      - TODO: Need to formalize exactly how 0th-order functions are defined and hoisted, such that we may have conditional occurence, higher-arity definitions, and a closed algebra for the composition of these.
      **
      
# Extensions, Nagging Comments and Concerns

* This borders on the idea of "deductive database systems", however we are building the DB from the ground (or above) up semi-automatically.  We are also allowing for "inductive" inferences via the use of models
* In the future, we should wrap up the whole thing in an HL-MRF to get or some meta-SRL model to provide for noisy integration
            
