// دالة لجمع القيم من الحقول المحددة
function sumValues(inputs) {
  let total = 0;
  inputs.forEach((input) => {
    total += parseFloat(input.value) || 0;
  });
  return total;
}

// دالة لحساب المجموعات وتحديثها في الصفحة
export function calculateTotals() {
  const quantityFields = document.querySelectorAll(".quantity");
  const totalPriceAfterTaxFields = document.querySelectorAll(
    ".total_price_after_tax"
  );

  const sumQuantity = sumValues(quantityFields);
  const sumTotalPriceAfterTax = sumValues(totalPriceAfterTaxFields);

  updateTotal("quantity", sumQuantity);
  updateTotal("total_price_after_tax", sumTotalPriceAfterTax);
}

// دالة لتحديث النتيجة على الصفحة
function updateTotal(elementId, total) {
  const totalField = document.getElementById(elementId);
  if (totalField) {
    if (totalField.tagName === "INPUT" && totalField.readOnly) {
      totalField.value = total.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    } else {
      totalField.textContent = total.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    }
  } else {
    console.warn(`Element with ID '${elementId}' not found.`);
  }
}

// حساب المجموع عند تحميل الصفحة
document.addEventListener("DOMContentLoaded", (event) => {
  calculateTotals();
});

// إضافة مستمعين لتحديث القيم عند تغيير الحقول
const inputs = document.querySelectorAll(".quantity, .total_price_before_tax");
inputs.forEach((input) => {
  input.addEventListener("input", calculateTotals);
});
