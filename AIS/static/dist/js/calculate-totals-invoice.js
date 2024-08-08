console.log("calculate-totals-invoice.js has been loaded");

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
  const discountFields = document.querySelectorAll(".discount");
  const taxValueFields = document.querySelectorAll(".tax_value");
  const totalPriceBeforeTaxFields = document.querySelectorAll(
    ".total_price_before_tax"
  );
  const totalPriceAfterTaxFields = document.querySelectorAll(
    ".total_price_after_tax"
  );

  const sumQuantity = sumValues(quantityFields);
  const sumDiscount = sumValues(discountFields);
  const sumTaxValue = sumValues(taxValueFields);
  const sumTotalPriceBeforeTax = sumValues(totalPriceBeforeTaxFields);
  const sumTotalPriceAfterTax = sumValues(totalPriceAfterTaxFields);

  updateTotal("quantity", sumQuantity);
  updateTotal("discount", sumDiscount);
  updateTotal("tax_value", sumTaxValue);
  updateTotal("total_price_before_tax", sumTotalPriceBeforeTax);
  updateTotal("total_price_after_tax", sumTotalPriceAfterTax);
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

 // إضافة مستمعين لتحديث القيم عند تغيير الحقول
  const inputs = document.querySelectorAll(".quantity, .total_price_before_tax");
  inputs.forEach((input) => {
    input.addEventListener("input", calculateTotals);
  });
