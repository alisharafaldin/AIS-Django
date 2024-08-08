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
      .innerHTML.replace(/form-\d+/g, `form-${formCount}`) // استبدال الأرقام في الحقول بترقيم النموذج الجديد
      .replace(/id_form-\d+-DELETE/g, `id_form-${formCount}-DELETE`); // استبدال معرف حقل DELETE

    // تفريغ قيم الحقول في النموذج الجديد
    const inputs = newForm.querySelectorAll(
      'input[type="text"], input[type="number"], input[type="hidden"]'
    );
    inputs.forEach((input) => {
      if (!input.name.endsWith("-id")) {
        input.value = ""; // تفريغ فقط الحقول غير الهامة
      }
    });

    container.appendChild(newForm); // إضافة النموذج الجديد إلى الـ container
    formCount++; // زيادة عداد النماذج
    totalForms.value = formCount; // تحديث عدد النماذج الإجمالي
    calculateTotals(); // تحديث المجموع بعد إضافة نموذج جديد
  });

  // إزالة نموذج
  container.addEventListener("click", function (event) {
    if (event.target.classList.contains("remove-form")) {
      event.preventDefault(); // منع السلوك الافتراضي للنقر على الزر
      const formContainer = event.target.closest(".form-container"); // العثور على أقرب عنصر بـ class 'form-container'
      const deleteInput = formContainer.querySelector('input[name$="-DELETE"]'); // العثور على حقل DELETE في النموذج
      if (!deleteInput) {
        const newDeleteInput = document.createElement("input");
        newDeleteInput.setAttribute("type", "hidden");
        newDeleteInput.setAttribute("name", `form-${formCount}-DELETE`);
        newDeleteInput.value = "on";
        formContainer.appendChild(newDeleteInput);
      } else {
        deleteInput.checked = true; // تحديد خانة حذف النموذج
        formContainer.style.display = "none"; // إخفاء النموذج من الواجهة
      }
      formCount--; // تقليل عداد النماذج
      totalForms.value = formCount; // تحديث عدد النماذج الإجمالي
    }
  });
});

