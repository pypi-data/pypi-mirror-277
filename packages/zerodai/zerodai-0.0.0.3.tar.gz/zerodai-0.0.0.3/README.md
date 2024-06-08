# Zerodai Library Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Method Descriptions](#method-descriptions)
   - [Inference](#inference)
   - [Function Calls (fn_c)](#function-calls-fn_c)
   - [Agent](#agent)
   - [Secondary Methods](#secondary-methods)
3. [Code Examples](#code-examples)
4. [Documentación en Español](#documentación-en-español)

### Introduction
The Zerodai library is designed to facilitate advanced cybersecurity and cyberintelligence operations through a series of specialized methods. This documentation aims to guide users of all levels, especially those new to Python or cybersecurity, through understanding and utilizing the powerful features of the Zerodai library.

### Method Descriptions

#### Inference
The `inference` method is a core component of the Zerodai library, allowing users to execute AI-driven analysis and response generation based on a set of input messages and specified functions. This method adapts its behavior based on the model specified, and can operate in either a streaming or non-streaming mode for real-time results.

#### Function Calls (fn_c)
`fn_c` is crucial for executing multiple cybersecurity tools or functions in a sequence, based on the complexity of the tasks required. It supports multistep operations, streaming output, and can dynamically adjust its processing based on the model and functions passed to it.

#### Agent
The `agent` method orchestrates complex interactions involving multiple tools and functions. It decides the flow of operations, handles execution, and manages error or output processing. This method is particularly useful for scenarios requiring a series of actions based on dynamic inputs and conditions.

#### Secondary Methods
Other methods such as `google`, `rubberducky_gen`, and `shodan_dork` are specialized functions designed for specific cybersecurity tasks like generating Google dorks or creating payloads for Rubber Ducky devices. These are explained in less detail but are crucial for targeted operations.










