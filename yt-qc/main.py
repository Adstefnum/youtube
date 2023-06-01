from qiskit import QuantumCircuit, Aer, execute

#quantum circuit with two quantum and two classical registers
qc = QuantumCircuit(2,2)

#applying the hadamard gate
#it puts qubit 0 into a superpostion between 0 and 1
#this means it now has an equal chance of being measured as 0 or 1
qc.h(0)

#control not gate
#a conditional 2 qubit gate
#it has control qubit and target qubit
#working: if state of control is 1 then you flip state of target qubit
#this causes a strong correlation between the states of the control adn target qubits leading to entanglement
qc.cx(0,1)

print(qc.measure_all())
#run a no of times and it has 50% chance of being 00 or 11 but not 01 or 10
#even though we didn't change state of 2nd qubit it still changed because of entanglemnt

simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1000)

# get the results and print them out
result = job.result()
counts = result.get_counts(qc)
print(counts)