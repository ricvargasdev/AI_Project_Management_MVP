customer = Customer(name="MHP")

project = Project(
    title="API Improvements",
    document=document,
    embedding=embedding
)

customer.projects.append(project)

session.add(customer)

session.commit()