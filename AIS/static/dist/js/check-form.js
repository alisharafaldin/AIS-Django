import { calculateTotals } from './calculate-totals.js';

const creditInputs = document.querySelectorAll(".credit-input");
const debitInputs = document.querySelectorAll(".debit-input");


// دالة للتحقق من وجود قيم في الحقول
function validateForm() {
    let hasValue = false;

    creditInputs.forEach((input) => {
      if (input.value.trim() !== "") {
        hasValue = true;
      }
    });
  
    debitInputs.forEach((input) => {
      if (input.value.trim() !== "") {
        hasValue = true;
      }
    });
  
    if (!hasValue) {
      alert("يجب إدخال قيمة في أحد الحقول المدين أو الدائن.");
      return false;
    }
  
    return calculateTotals();
  }
  validateForm();
  