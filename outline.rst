

Neo: a universal object model for handling electrophysiology data in multiple formats



Introduction
========

  * diversity of analyses/acquisition/plotting systems and lack of interoperability
  * bridge between experimentalists' and modelers' tools
  * replication of effort for reading/converting data
  * existing tools, their limitations:
     - neuroshare
     - biosig
  * need to have a model object that embraces complexity of data (heterogeneity, etc.)
  * open source
  

Design considerations
==============

  * best practice : units and important metadata (sampling_rate, t_start, ..)
  * heterogeneity of data
  * assymmetry of data
  * scope : data objects only (no visulization or analysis methods)
  * data can be in chunks : we need a Segment object
  * compatibility with other scientific libraries 
  * efficiency for arrays

Object model
=========

description
------------------

  * 3 types : data objects/container objects/grouping objects
  * 3 types of attributes : required, recommended, and additional
  * scalar vs non scalar (very briefly)
  * enumeration of objects
  * relationships (one to many, many to many)

Figure 1 : all object in colors (same as doc)
Figure 2 : relational schema (new one from scratch)


Implementation in python.
---------------------------------------

  * numpy and quantities
  * classes that inherit from quantities : arguments for and against the choice to use inheritance
  * annotations in dict
  * initialization (required, recommended, and additional)
  * relationships - with python list (simple but comes with limits)



Read/write datasets
=============

reformulate neo.io documentation

description
------------------

  * API flexible because heterogenous data format
  * one class = one format
  * mode explenation :  file/dir/database (different karg in __init__)
  * Supported objects/readable objects  (monolitic read vs partial reading)
  * Lazy reading concept (include Robert's proposal for post reading lazy object)
  * cascade reading concept


Implementation in python.
---------------------------------------

  * use memmap when possible
  * explanation for proprietary formats : reverse engineering + version formats problem

Unittest and continuous integration
-------------------------------------------------------

  * mention python unittest
  * travis
  * files at g-node for all formats
  



Usage examples
===========

More or less Use case in doc


  * Recording multiple trials from multiple channels = acces by Segment or acces by Channel
  * Recording spikes from multiple tetrodes

Figure 3:  multi_segment_diagram_with_analogsignal
Figure 4: multi_segment_diagram_with_spiketrain_and_units



Discussion
=======


Impact : projects using neo
-----------------------------------------
  
  * impact (major or null) depends on whether adopted or not
  * brief intro on sustainability (several lab and several dev)

Each dev write some lines for their project, then we can eliminate redunduancies between accounts

  * PyNN 
  * Mozaik
  * SpikeViewer
  * OpenElectrophy : the RecordingChannelGroup and RecordingChannel that facilitate the spike sorting flexibility (aggregate channel in polytrode)
  * Helmholtz
  * Elphy case at lab scale.


Current limits
------------------

  * Model will change
  * Performance limits
  * IO everything in mem.
  * Objects representing analysis outputs ? Only raw data at the moment.

