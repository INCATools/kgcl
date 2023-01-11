# KGCL Commands.

## `NodeRename`:
	Command using CURIEs: `rename GO:0005635 from 'nuclear envelope' to 'foo bar'`
	Command using URIs: `rename http://purl.obolibrary.org/obo/GO_0005635 from 'nuclear envelope' to 'foo bar'`

## `NodeObsoletion`:
	Command using CURIEs: `obsolete GO:0005634`

## `NodeObsoletionWithDirectReplacement`:
	Command using CURIEs: `obsolete GO:0005634 with replacement GO:999`

## `NewSynonym`:
	Command using CURIEs: `create exact synonym 'foo' for GO:0005634`
	Command using URIs: `create exact synonym 'foo' for http://purl.obolibrary.org/obo/GO_0005634`

## `ClassCreation`:
	Command using CURIEs: `create GO:9999999`
	Command using URIs: `create http://purl.obolibrary.org/obo/GO_9999999`

## `NodeCreation`:
	Command using CURIEs: `create node GO:9999999 'foo'`

## `EdgeCreation`:
	Command using CURIEs: `create edge GO:0005634 BFO:0000050 GO:0009411`
	Command using URIs: `create edge http://purl.obolibrary.org/obo/GO_0005634 http://purl.obolibrary.org/obo/BFO_0000050 http://purl.obolibrary.org/obo/GO_0009411`

## `PlaceUnder`:
	Command using CURIEs: `create edge GO:0005634 rdfs:subClassOf GO:0009411`
	Command using URIs: `create edge http://purl.obolibrary.org/obo/GO_0005634 http://www.w3.org/2000/01/rdf-schema#subClassOf http://purl.obolibrary.org/obo/GO_0009411`

## `PredicateChange`:
	Command using CURIEs: `change relationship between GO:0005635 and GO:0005634 from BFO:0000050 to rdfs:subClassOf`

## `RemoveUnder`:
	Command using CURIEs: `delete edge GO:0005634 rdfs:subClassOf GO:0043231`
	Command using URIs: `delete edge http://purl.obolibrary.org/obo/GO_0005634 http://www.w3.org/2000/01/rdf-schema#subClassOf http://purl.obolibrary.org/obo/GO_0043231`

## `EdgeDeletion`:
	Command using CURIEs: `delete edge GO:0005635 BFO:0000050 GO:0005634`

## `NodeDeepening`:
	Command using CURIEs: `deepen GO:0005739 from GO:0043231 to GO:0005634`

