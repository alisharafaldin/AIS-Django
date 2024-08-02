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
  const quantity = document.querySelectorAll(".quantity");
  const discount = document.querySelectorAll(".discount");
  const tax_value = document.querySelectorAll(".tax_value");
  const total_price_before_tax = document.querySelectorAll(".total_price_before_tax");
  const total_price_after_tax = document.querySelectorAll(".total_price_after_tax");

  const t_quantity = sumValues(quantity);
  const t_discount = sumValues(discount);
  const t_tax_value = sumValues(tax_value);
  const t_total_price_before_tax = sumValues(total_price_before_tax);
  const t_total_price_after_tax = sumValues(total_price_after_tax);


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