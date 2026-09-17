from fastapi import FastAPI, Body, FastAPI, APIRouter, status, HTTPException
from schema.expensesList import expenses
from schema.incomeList import income
import routes.expensesRoutes as expensesRoutes
import routes.incomeRoutes as incomeRoutes

app = FastAPI()

app.include_router(expensesRoutes.router)
app.include_router(incomeRoutes.router)

router = APIRouter(prefix="/api/analysis", tags=["Analysis"])


# Method: GET
# Route: api/analisis
# Description: analise expenses based on income
@router.get("/", status_code=status.HTTP_200_OK)
def analysis():

    if not income:
        raise HTTPException(status_code=400, detail="No income...")

    if not expenses:
        raise HTTPException(status_code=400, detail="No expenses...")

    totalIncome = sum(x.ammount for x in income)
    totalExpenses = sum(x.ammount for x in expenses)
    res = totalIncome - totalExpenses

    return {
        "message": f"Based on your income and expenses, you have left ${res} per month"
    }


app.include_router(router)
