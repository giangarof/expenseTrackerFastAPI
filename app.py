from fastapi import FastAPI, Body, FastAPI, APIRouter

app = FastAPI()
router = APIRouter(prefix="/api/expenses")

expenses = [
    {"id": 1, "name": "rent", "ammount": 550},
    {"id": 2, "name": "gas", "ammount": 80},
    {"id": 3, "name": "insurance", "ammount": 120},
    {"id": 4, "name": "food", "ammount": 220},
]


# Method: GET
# Route: api/expenses/home
# Description: Home route
@router.get("/home")
def home():
    return {"message": "This app is to display all your expenses"}


# Method: GET
# Route: api/expenses/
# Description: Retrieve all expenses
@router.get("/")
def getAll():
    if not expenses:
        return {"message": "no expenses available"}
    return {"message": "All expenses", "data": expenses}


# Method: GET
# Route: api/expenses/{id}
# Description: Retrieve one expense by id
@router.get("/{id}")
def getOneById(id: int):
    for x in expenses:
        if x["id"] == id:

            return {"message": "Expense found", "data": x}

    return {"message": "Id doesnt exist"}


# Method: POST
# Route: api/expenses/
# Description: Add a new employee
@router.post("/")
def addNewExpense(data=Body()):
    if not data:
        return {"message": "No data provided"}
    if len(expenses) == 0:
        data["id"] = 1

    data["id"] = expenses[-1]["id"] + 1

    expenses.append(data)
    return {"message": "Expense added", "data": data}


# Method: PUT
# Route: api/expenses/update/{id}
# Description: Update a employee by id
@router.put("/update/{id}")
def updateById(id: int, data=Body()):

    # find id first
    for x in expenses:
        # if it does exist, update name and ammount
        if x["id"] == id:
            # First way
            # x["name"] = data["name"]
            # x["ammount"] = data["ammount"]

            # Second way
            x.update({"name": data["name"], "ammount": data["ammount"]})
            return {"message": "Updated successfully", "data": data}

    return {"message": "No found"}


# Method: DELETE
# Route: api/expenses/delete/{id}
# Description: Delete a employee by id
@router.delete("/{id}")
def deleteById(id: int):
    # find id first
    for x in expenses:
        # if it does exist, then delete the expense
        if x["id"] == id:
            expenses.remove(x)
            return {"message": "Expense deleted successfully"}
    return {"message": "Id doesnt exist"}


app.include_router(router)
