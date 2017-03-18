# On Defining Tasks

We view all questions that can be asked about a document as a function of the text. This is not necessarily a truism, from the data collection perspective. 
This is because previously, IE has subdivided function-type-equivalent questions about into semantic clusters. For the purposes of defining an IE system though, this is actually unnecessary.

### How Information Extraction (IE) tasks are currently thought about

In previous formalisms of tasks for IE, we break down questions about documents into semantic clusters of extractions. 
Historically, this was necessary for the design of domain-specific systems that aimed build pipelines of submodules each addressing these tasks.
Additionally these types of distinctions provide manageable chunks of IE subproblems for the research community to focus on. 
Especially when building a good IE pipeline required years of extensive feature engineering, domain, ML, and linguistic expertise, and pretrained NLP tools.

Here is an sample list of many of these semantic "sub-tasks":

1. Named Entity Recognition
2. Value Recognition
3. Relation Identification and Classification (Relation Extraction if all at once)
4. Event Trigger Identification and Classification
5. Event Argument Detection
6. Within Document Named Entity Coreference
7. Within Document Event Coreference
8. Named Entity Property Categorization
9. Relation Property Categorization
10. Event Trigger Property Categorization
11. Event Argument Property Categorization
12. Named Entity Disambiguation to an outside source (also known as Wikification, Record Deduplication, Entity Resolution, Entity Linking, etc)
13. Event Disambiguation to an outside source (also known as Cross-Document Event Coreference, Event Discovery, Event Linking, etc)
14. Value Normalization (i.e., TIMEX)

Yet, these distinctions are unnecessary with respect to the functionality of what and IE system aims to achieve. 
At the end of the day, IE systems (should) aim to answer queries of interest about document collections.
These queries typically cover highly variable level of semantic granularity and analysis.

Here is an example set of questions a domain expert may have about a document collection (from high to mid semantic level): 

* "What are the terror attacks expressed in this collection of news documents?"
* "Which countries where the agents of terror attacks from?"
* "When did these terror attacks occur?"
* "Did a terror attack occur between October and Novermber, 2015?"
* "If so, how many people were killed or critically injured?"

These are obviously far too high level for a program to answer with any real accuracy. 
They involve classification of subqueries over entire document collections.
So as IE task creators, we break them down into constituent subqueries recursively until we can reach something that is manageable for an algorithm (the pipeline we have in mind) to understand. 
We then answer these high level queries through bottom-up logical composition and aggregation (aka reasoning or queries) of atomic factual units.
If we break the notion of "atomic factual units" down enough, we get entity and relation extraction.
This is not surprising. Just as people do, we can compose factual assertions about sets of a few basic objects in the world 
and how they interact with/operate on eachother to answer virtually infinitely varying questions of increasing complexity.
(As people, we then "chunk" the answers to subqueries so that we can answer even higher level questions later on with less mental effort. We memoize...)

Putting it as annoyingly simply as possible: Language is compositional.

So why this rant?

This means IE tasks at the end of the day are logical composition of entities and their interactions. 
Here, for the purpose of defining IE tasks, it becomes very useful to blend all of the semantic distinctions of the first list.
I use entities to refer to any type "object" that is being communicated through language. These "objects" can have any granularity. 
They could be a single atom, a cell, a body part, a person, a group of people, etc.
In IE, we call these interactions between real world objects "relations." 
Under the typical formalism of IE, relations are functions of arity 2 (they take two arguments.)
But I see this as an narrow definition.
I view relations as objects which have a functional component. They have a domain and range.
It is easy to see why this must be necessary once you begin to talk about events.

Viewing events as interactions (i.e., higher-arity functions) immediately is troubled by their non-compact representation.
Since mathematically functions do not have optional arguments (changing arguments necessarily makes it a different function,)
we need to represent every possible combination of arguments for an interaction separately. This is exponential/non-compact and thus not useful.
But if we instead view events as abstract objects (Neo-Davidsonian reification,) we now have a compact representation. 
The event interacts with each of its arguments through a separate arity-2 relation.
However if these relations can have additional arguments, we must again recursively define them as events to remain compact.

My point is that relations and events, henceforth refered to as "interactions" are themselves a subset of objects, such that they have a domain and range. Domain and range are objects themselves (but they are base cases -- primitive objects.)

All properties of objects now begin to look like objects themselves; their domain and range are sets of objects defined by some common set of shared properties (as is the case in math when we define sets -- things are in the set conditional on them satisfying certain properties.)

Ok, so what's the punchline?

The punchline is that we have fully recursed. Our basic building blocks are objects, that's it. We can now define any information extraction task as the identification of some "interesting" set of objects and the dependencies they can share through their operation on eachother as functions, according to compatible domain and range constraints. 

I am by no means even close to the first person to recover this basic notion of composition. It has been paid great attention throughout the history of philosophy, linguistics, and cognitive science.
** TODO: List a bunch of historical references that are concerned with this idea

We even have a fully thought out ecosystem of storing information in this totally general interoperable way: RDF.
And the RDF community has built on this idea immensely. The basic primitives, RDFSchema, encode precisely the notions I've described above, and the basic/primitive objects that serve to as the basic composition functions that can produce the infinite expressiveness of logic when coupled with actualizations of bottom-level inputs.

My only claim of novelty here is that we should also be following these notions when considering how to build end-to-end IE systems. We should keep this generality in mind when building a framework that aims to provide build-your-own-IE-system functionality.

It will be up to the creator fo the tasks, the domain expert, to decompose their analytical questions into the appropriate atomic units (for now.) They will still need to define which objects are interesting, and in what contexts (of other present objects.) They will still have to define which interactions are interesting as well.  

But what they don't need to do is break these notions down into semantic sub-tasks, each with their own annotation constraints. We will automatically do this, but in a very lightweight and general way.

Here is a (progressively) concrete prescription (after this absurdly abstract diatribe...):

Users should try to reach their task definitions using a top-down approach. They should ask the biggest questions they hope to answer. Then they should break down these questions into logical composition of sets of entities. Then for any entity that is not sufficiently fine-grained to annotate (i.e., it is still the result of an actualized subquery/has a compositional definition) they should again break it down into its constiuent pieces.  They should do this recursively until there are no underdefined entities/interactions to annotate.

Once they have done so, it is simply a matter of specifying in which situations are the extraction of entities "interesting" (i.e., useful in answering their questions).

From these definitions we can do the rest of the work.

* Any entities which are interesting on their own (independent on the presence of other entities) are the basic entities.
* Any entities 




