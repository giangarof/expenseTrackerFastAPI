from fastapi import FastAPI, Body, FastAPI, APIRouter, status, HTTPException
from schema.expensesList import expenses, expensesEmpty
from schema.Expenses import Expenses, ExpenseRequest
from utils import newId

router = APIRouter(prefix="/api/expenses", tags=["Expenses"])


# Method: GET
# Route: api/expenses/
# Description: Retrieve all expenses
@router.get("/", status_code=status.HTTP_200_OK)
def getAll():
    if not expenses:
        raise HTTPException(status_code=404, detail="no expenses available")
    return {"message": "All expenses", "data": expenses}


# Method: GET
# Route: api/expenses/
# Description: Get total of your expenses
@router.get("/gettotal", status_code=status.HTTP_200_OK)
def getTotal():
    if not expenses:
        raise HTTPException(status_code=404, detail="no expenses available")
    total = sum(x.ammount for x in expenses)
    return {"message": "Your total Expenses", "data": total}


# Method: GET
# Route: api/expenses/{id}
# Description: Retrieve one expense by id
@router.get("/{id}", status_code=status.HTTP_200_OK)
def getOneById(id: int):
    for x in expenses:
        if x.id == id:

            return {"message": "Expense found", "data": x}

    raise HTTPException(status_code=404, detail="Id doesnt exist")


# Method: POST
# Route: api/expenses/
# Description: Add a new expense
@router.post("/", status_code=status.HTTP_201_CREATED)
def addNewExpense(expenseRequest: ExpenseRequest):
    # print(expenseRequest.name)
    if not expenseRequest:
        raise HTTPException(status_code=404, detail="No data provided")

    newExpense = Expenses(newId(expenses), expenseRequest.name, expenseRequest.ammount)

    expenses.append(newExpense)
    return {"message": "Expense added", "data": expenseRequest}


# Method: PUT
# Route: api/expenses/update/{id}
# Description: Update a employee by id
@router.put("/update/{id}", status_code=status.HTTP_200_OK)
def updateById(id: int, expenseRequest: ExpenseRequest):

    # find id first
    for x in expenses:
        # if ID does exist, update name and ammount
        if x.id == id:
            x.name = expenseRequest.name
            x.ammount = expenseRequest.ammount

            return {"message": "Updated successfully", "data": expenseRequest}

    raise HTTPException(status_code=404, detail="No found")


# Method: DELETE
# Route: api/expenses/delete/{id}
# Description: Delete a employee by id
@router.delete("/{id}", status_code=status.HTTP_200_OK)
def deleteById(id: int):
    # find id first
    for x in expenses:
        # if it does exist, then delete the expense
        if x.id == id:
            expenses.remove(x)
            return {"message": "Expense deleted successfully"}
    raise HTTPException(status_code=404, detail="Id doesnt exist")
