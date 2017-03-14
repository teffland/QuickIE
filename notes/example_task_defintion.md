# Example of Defining a Task

In this example, we illustrate how to define the set of tasks for an application by drilling down questions.

The example application is the monitoring of online restaurant reviews for outbreaks of foodborne illness.

We can create/uncover task definitions by walking through a series of questions that we'd ask about a document or corpora.
For each question, we try to write to it's equivalent as a logical statement (using a pseudo notation).
This will usually be the logical combination of the results of subqueries.
Then for every undefined subquery, we try to define it.  
We do so recursively, until our definitions contain only logic and basic functions (through bottom-up substitution).
Then we know exactly the set of functions we need to be able to answer to build our set of defined queries.

**Notation:** 
```
"<Some question about data>?"(input) --> <pseudo logic>
```
or
```
"<Some question about data>?"(input) --> {
  <multiline pseudo logic>
}
```

#### Question Types:
* Questions about containers, subsets, groupbys, filters
* Questions about the existence of (composite) entities
* Questions about the definition of (composite) entites

** IS a Container different than a Composite Entity? Not clear right now...**

1. "Are there any outbreaks of foodborne illenss"? Are there more than 0 outbreaks of foodborne illness
2. "What are outbreaks of foodborne illness"? When more than one person gets food poisoning at the same restaurant within a week of eachother.
3. What is a "person"? I'll show you => (Taggable)
4. What is food poisoning? Food poisoning is when a person gets sick from eating food
5. What is "gets sick"? I'll show you => (Taggable)
6. What is a "restaurant"? --> Taggable
7. What is a "within a week"? When the difference between to absolute times is greater than some amount of relative time
  -> Absolute Times
  -> Relative Times
 
 
Task Basic Types so far:
- Person
- Restaurant/Place
- Absolute Time
- Relative Time
- Symptom
- Food

Relations/Events
- Person.Ate.Food === Ate.subject.Person, Ate.object.Food
- Sick.subject.Person === Sick.agent.Person
- Sick.FromEating.Ate
- Ate.Start.Time
- Ate.End.Time
- Ate.At.Place

* Conditional annotation questions can be answered by one-sided expert annotation cooccurrence
* Nagging question: in Rich ERE, entities and events must have explict trigger/head tags, while relations only need implicit connections and have extents
  - Under a nested/hierarchical tagging model this is not a problem, provided you tag the extents, 
  or you need a model that can treat implicit relations as neo-davidsonian when they have other potential arguments or properties
* What about properties and their evidence. They are obviously conditional.
* Every type of annotation should be allowed to have a head and extent annotated for it

TODO:
* [ ] - implement a virtuoso db with a document collection
* [ ] - parse each document into List of sentences
* [ ] - define rdf meta types, including doc, annotator, domain, task, etc...
* [ ] - implement script that infers label typeset given the description in YAML

* [ ] - (Can this just be using BRAT)? implement monolithic view that shows abridged list of pipeline questions and pageable docs
  * [ ] - implement document search
  * [ ] - implement mention highlighting
  * [ ] - implement mention property submenu
  * [ ] - implement relation drag-and-drop

* [ ] - implement microtask view of documents
  * [ ] - implement document sentence context showing
  * [ ] - implement mention highlighting


1. "Are there any outbreaks of foodborne illness"?(Documents) --> return count("What are the outbreaks of foodborne illness"?(Documents)) > 0
2. "What are the outbreaks of foodborne illness"?(Documents) --> {
  return select * from outbreaks(Documents)
}
3. "What is an outbreak"?(Documents) --> {
  //An outbreak is when more than one person gets food poisoning at the same place within a week of eachother.
  Outbreak := sum(count(fp.people) for fp in Which food poisoning events occured 
}




### Basic Types:

** TODO: This notation should be formalized using [rdfs](https://www.w3.org/TR/rdf-schema/) or even potentially [OWL](https://www.w3.org/TR/rdf-schema/#bib-OWL2-OVERVIEW)instead **

* `../Object`
  * `Property/UID := unique int`
  * `Property/Description :opt= str`
  
* `../Object/Creator`
  * `Property/Name :opt= str`
  
* `../Object/Function` // an abstract function definition
  * `Property/Domain := ../Object *` // can take in any number of object arguments
  * `Property/Range := ../Object *`  // can emit any number of object arguments
  * `Property/Creator := ../Object/Creator
  <!-- * Actualizable -->
  
* `../Object/Function/Is` // generic relation for equivalence/cross-hierarchy conditional inheritance
* `../Object/Function/Contains` // generic relation for ownership, reserved for sets
  * `Property/Domain := ../Object/Set`
  
* `../Object/Set` // a container object
  * `../Object/Function/Contains := ../Object *` // can contain any number of objects
  * `Property/type := ../Object/..` // all contains must satisfy some global level of type
  
