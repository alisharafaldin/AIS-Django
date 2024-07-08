// دالة لجمع القيم من الحقول المحددة
function sumValues(inputs) {
  let total = 0;
  inputs.forEach((input) => {
    total += parseFloat(input.value) || 0;
  });
  return total;
}

// دالة لحساب المجموعات والفرق بينها
export function calculateTotals() {
  const creditInputs = document.querySelectorAll(".credit-input");
  const debitInputs = document.querySelectorAll(".debit-input");

  const totalCredit = sumValues(creditInputs);
  const totalDebit = sumValues(debitInputs);
  const difference = totalCredit - totalDebit;

  const result = document.getElementById("result");
  if (difference !== 0) {
      result.style.color = "red";
      result.textContent = `التوازن غير صحيح. فرق ${difference.toFixed(2)}`;
    } else {
      result.style.color = "green";
      result.textContent = `التوازن صحيح.`;
    }

    updateTotal("total-c", totalCredit);
    updateTotal("total-d", totalDebit);
    updateTotal("result", difference);

    return difference === 0;  // نحتاج إلى إعادة قيمة صحيحة إذا كان التوازن صحيحًا
}

// دالة لتحديث النتيجة على الصفحة
function updateTotal(elementId, total) {
  const totalField = document.getElementById(elementId);
  totalField.textContent =
    `${elementId.replace(/-/g, " ").toUpperCase()}: ` + total.toFixed(2);
}

// حساب المجموع عند تحميل الصفحة
document.addEventListener("DOMContentLoaded", (event) => {
  calculateTotals();
});