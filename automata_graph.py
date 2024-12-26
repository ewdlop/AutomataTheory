#!/usr/bin/env python3#

#!pip install pip install graphviz

from graphviz import Digraph

def generate_fsm():
    # Create a new directed graph
    fsm = Digraph('finite_state_machine')

    # Add nodes (states)
    fsm.node('A', 'State A')
    fsm.node('B', 'State B')
    fsm.node('C', 'State C')

    # Add edges (transitions)
    fsm.edge('A', 'B', label='0')
    fsm.edge('A', 'C', label='1')
    fsm.edge('B', 'A', label='0')
    fsm.edge('B', 'C', label='1')
    fsm.edge('C', 'C', label='0,1')

    # Save and render the graph
    fsm.render('fsm', format='png', cleanup=True)

    return fsm

# Generate and view the FSM
fsm = generate_fsm()
fsm.view()

def generate_pda():
    # Create a new directed graph
    pda = Digraph('pushdown_automaton')

    # Add states
    pda.node('q0', 'q0')
    pda.node('q1', 'q1')
    pda.node('q2', 'q2')

    # Add transitions
    pda.edge('q0', 'q1', label='a, ε → A')
    pda.edge('q1', 'q1', label='b, A → ε')
    pda.edge('q1', 'q2', label='ε, $ → ε')

    # Save and render the graph
    pda.render('pda', format='png', cleanup=True)

    return pda

# Generate and view the PDA
pda = generate_pda()
pda.view()

def generate_tm():
    # Create a new directed graph
    tm = Digraph('turing_machine')

    # Add states
    tm.node('q0', 'q0')
    tm.node('q1', 'q1')
    tm.node('q2', 'q2')

    # Add transitions
    tm.edge('q0', 'q1', label='a → X, R')
    tm.edge('q1', 'q1', label='b → Y, R')
    tm.edge('q1', 'q2', label='c → Z, L')

    # Save and render the graph
    tm.render('tm', format='png', cleanup=True)

    return tm

# Generate and view the TM
tm = generate_tm()
tm.view()
