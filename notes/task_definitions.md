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
So as IE task creators, we break them down into constituent subqueries recursively until we can reach something that is manageable for an algorithm to understand. 
We then answer these high level queries through bottom-up logical composition and aggregation (aka reasoning or queries) of atomic factual units.
If we break the notion of "atomic factual units" down enough, we get entity and relation extraction.
This is not surprising. Just as people do, we can compose factual assertions about sets of a few basic objects in the world 
and how they interact with/operate on eachother to answer virtually infinitely varying questions of increasing complexity.
(As people, we then "chunk" the answers to subqueries so that we can answer even higher level questions later on with less mental effort. We memoize...)

So why this rant?

This means IE tasks at the end of the day are logical composition of entities and their interactions. 
Here, it becomes very useful to blend all of the semantic distinctions of the first list.
I use entities to refer to any type "object" that is being communicated through language. These "objects" can have any granularity. 
They could be a single atom, a body part, a person, a group of people, etc.
In IE, we call these interactions between real world objects "relations." 
Under the typical formalism of IE, relations are functions of arity 2 (they take two arguments.)
But I see this as an narrow definition.
I view relations as objects which have a functional component. They have a domain and range.
It is easy to see this once you begin to talk about events.

Viewing events as interactions (i.e., higher-arity functions) immediately is troubled by their non-compact representation.
Since mathematically functions do not have optional arguments (changing arguments necessarily makes it a different function,)
we need to represent every possible combination of arguments for an interaction separately. This is exponential and thus not easily learnable.
But if we instead view events as abstract objects (Neo-Davidsonian reification,) we now have a compact representation. 
The event interacts with each of its arguments through a separate arity-2 relation.
However if these relations can have additional arguments, we must again recursively define them as events to remain compact.

My point is that relations and events, henceforth refered to as "interactions" are themselves a subset of objects, such that they have a domain and range.

Properties of objects now begin to look like objects themselves, 

Additionally, these objects themselves can affect eachother, so they are also "functions" with 
