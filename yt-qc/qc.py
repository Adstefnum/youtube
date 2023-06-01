from qiskit import QuantumCircuit, Aer, execute

qc = QuantumCircuit(2,2)

qc.h(0)

#00 11 not 10 or 01
qc.cx(0,1)

qc.measure_all()

simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=1000)

result = job.result()
counts = result.get_counts(qc)
print(counts)