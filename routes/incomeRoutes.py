from fastapi import FastAPI, Body, FastAPI, APIRouter, status, HTTPException
from schema.expensesList import expenses, expensesEmpty
from schema.incomeList import income, emptyIncome
from schema.Expenses import Expenses
from schema.Income import Income, IncomeRequest
from utils import newId

router = APIRouter(prefix="/api/income", tags=["Income"])


# Method: GET
# Route: api/income
# Description: Get all incomes
@router.get("/", status_code=status.HTTP_200_OK)
def getTotalIncome():

    if not income:
        raise HTTPException(
            status_code=404,
            detail="You dont have income. Try and add your current income",
        )
    total = sum(x.ammount for x in income)

    if total < 1:
        raise HTTPException(
            status_code=404, detail="Your income is equal/bellow zero..."
        )
    return {"message": "Current income found", "data": total}


# Method: GET
# Route: api/income/getall
# Description: Get all incomes
@router.get("/getall", status_code=status.HTTP_200_OK)
def displayAllIncome():
    if not income:
        raise HTTPException(
            status_code=404,
            detail="You dont have income. Try and add your current income",
        )

    return {"message": "Current income found", "data": income}


# Method: POST
# Route: api/income
# Description: Add income
@router.post("/", status_code=status.HTTP_201_CREATED)
def addIncome(incomeRequest: IncomeRequest):

    newIncome = Income(newId(income), incomeRequest.name, incomeRequest.ammount)

    income.append(newIncome)
    return {"message": "Income added", "data": newIncome}


# Method: PUT
# Route: api/income
# Description: Update income by id
@router.put("/update/{id}", status_code=status.HTTP_200_OK)
def updateIncome(id: int, incomeRequest: IncomeRequest):

    # find id first
    for x in income:
        # if ID does exist, update name and ammount
        if x.id == id:
            x.name = incomeRequest.name
            x.ammount = incomeRequest.ammount

            return {"message": "Income updated successfully", "data": incomeRequest}

    raise HTTPException(status_code=404, detail="No found")


# Method: DELETE
# Route: api/income/{id}
# Description: Delete an income by id
@router.delete("/{id}", status_code=status.HTTP_200_OK)
def deleteById(id: int):
    for x in income:
        if x.id == id:
            income.remove(x)
            return {"message": "Income deleted successfully", "data": x}

    raise HTTPException(status_code=404, detail="id doesnt exist")
