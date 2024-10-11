import { calculateTotals } from "./calculate-totals-invoice.js";

console.log("add-remove-invoice-form.js has been loaded");

document.addEventListener("DOMContentLoaded", function () {
  const container = document.getElementById("formset-container");
  const addButton = document.getElementById("add-form");
  const totalForms = document.getElementById("id_form-TOTAL_FORMS");

  let formCount = parseInt(totalForms.value);

  // إضافة نموذج جديد
  addButton.addEventListener("click", function () {
    const newForm = document.createElement("tr"); // إنشاء عنصر <tr> جديد
    newForm.classList.add("form-container"); // إضافة الكلاس 'form-container' للعنصر الجديد
    newForm.innerHTML = container
      .querySelector(".form-container")
      .innerHTML.replace(/form-\d+/g, `form-${formCount}`)
      .replace(/id_form-\d+-DELETE/g, `id_form-${formCount}-DELETE`); // استبدال الأرقام في الحقول بترقيم النموذج الجديد
    // تفريغ قيم الحقول في النموذج الجديد
    const inputs = newForm.querySelectorAll('input[type="hidden"]');
    inputs.forEach((input) => {
      input.value = ""; // تفريغ قيمة الحقل
    });
    container.appendChild(newForm); // إضافة النموذج الجديد إلى الـ container
    formCount++; // زيادة عداد النماذج
    totalForms.value = formCount; // تحديث عدد النماذج الإجمالي
    calculateTotals(); // تحديث المجموع بعد إضافة نموذج جديد
  });

  // دالة لحذف نموذج
  container.addEventListener("click", function (event) {
    if (event.target.classList.contains("remove-form")) {
      event.preventDefault(); // منع السلوك الافتراضي للنقر على الزر
      const formContainer = event.target.closest(".form-container"); // العثور على أقرب عنصر بـ class 'form-container'
      const deleteInput = formContainer.querySelector('input[name$="-DELETE"]'); // العثور على حقل DELETE في النموذج
      if (deleteInput) {
         // تفريغ الحقول quantity و total_price_after_tax قبل حذف النموذج
         const quantityInput = formContainer.querySelector(".quantity");
         const total_price_after_taxInput = formContainer.querySelector(".total_price_after_tax");
         if (quantityInput) quantityInput.value = "0";
         if (total_price_after_taxInput) total_price_after_taxInput.value = "0";
        calculateTotals(); // تحديث المجموع بعد إزالة نموذج
        deleteInput.checked = true; // تحديد خانة حذف النموذج
        formContainer.style.display = "none"; // إخفاء النموذج من الواجهة
      } else {
        formContainer.remove(); // إزالة النموذج من الواجهة
        formCount--; // تقليل عداد النماذج
        totalForms.value = formCount; // تحديث عدد النماذج الإجمالي
        calculateTotals(); // تحديث المجموع بعد إزالة نموذج
      }
    }
  });

});
