


### **Approach 1: Basic Form Handling with Local State**

```jsx
import React, { useState } from "react";

const DynamicForm = () => {
  const [formData, setFormData] = useState({ name: "", email: "", password: "" });
  const [errors, setErrors] = useState({});

  const validate = () => {
    const newErrors = {};
    if (!formData.name) newErrors.name = "Name is required.";
    if (!formData.email) {
      newErrors.email = "Email is required.";
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      newErrors.email = "Invalid email format.";
    }
    if (formData.password.length < 6) newErrors.password = "Password must be at least 6 characters.";
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validate()) alert("Form submitted successfully!");
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Name:</label>
        <input
          type="text"
          value={formData.name}
          onChange={(e) => setFormData({ ...formData, name: e.target.value })}
        />
        {errors.name && <small>{errors.name}</small>}
      </div>
      <div>
        <label>Email:</label>
        <input
          type="email"
          value={formData.email}
          onChange={(e) => setFormData({ ...formData, email: e.target.value })}
        />
        {errors.email && <small>{errors.email}</small>}
      </div>
      <div>
        <label>Password:</label>
        <input
          type="password"
          value={formData.password}
          onChange={(e) => setFormData({ ...formData, password: e.target.value })}
        />
        {errors.password && <small>{errors.password}</small>}
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default DynamicForm;
```

---

### **Approach 2: Reusable Input Component**

```jsx
import React, { useState } from "react";

const InputField = ({ label, type, value, onChange, error }) => (
  <div>
    <label>{label}:</label>
    <input type={type} value={value} onChange={onChange} />
    {error && <small>{error}</small>}
  </div>
);

const DynamicForm = () => {
  const [formData, setFormData] = useState({ name: "", email: "", password: "" });
  const [errors, setErrors] = useState({});

  const validate = () => {
    const newErrors = {};
    if (!formData.name) newErrors.name = "Name is required.";
    if (!formData.email) {
      newErrors.email = "Email is required.";
    } else if (!/\S+@\S+\.\S+/.test(formData.email)) {
      newErrors.email = "Invalid email format.";
    }
    if (formData.password.length < 6) newErrors.password = "Password must be at least 6 characters.";
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validate()) alert("Form submitted successfully!");
  };

  return (
    <form onSubmit={handleSubmit}>
      <InputField
        label="Name"
        type="text"
        value={formData.name}
        onChange={(e) => setFormData({ ...formData, name: e.target.value })}
        error={errors.name}
      />
      <InputField
        label="Email"
        type="email"
        value={formData.email}
        onChange={(e) => setFormData({ ...formData, email: e.target.value })}
        error={errors.email}
      />
      <InputField
        label="Password"
        type="password"
        value={formData.password}
        onChange={(e) => setFormData({ ...formData, password: e.target.value })}
        error={errors.password}
      />
      <button type="submit">Submit</button>
    </form>
  );
};

export default DynamicForm;
```

---

### **Approach 3: Form Handling with `useReducer`**

```jsx
import React, { useReducer } from "react";

const initialState = { name: "", email: "", password: "", errors: {} };

const reducer = (state, action) => {
  switch (action.type) {
    case "SET_FIELD":
      return { ...state, [action.field]: action.value };
    case "SET_ERRORS":
      return { ...state, errors: action.errors };
    default:
      return state;
  }
};

const DynamicForm = () => {
  const [state, dispatch] = useReducer(reducer, initialState);

  const validate = () => {
    const newErrors = {};
    if (!state.name) newErrors.name = "Name is required.";
    if (!state.email) {
      newErrors.email = "Email is required.";
    } else if (!/\S+@\S+\.\S+/.test(state.email)) {
      newErrors.email = "Invalid email format.";
    }
    if (state.password.length < 6) newErrors.password = "Password must be at least 6 characters.";
    dispatch({ type: "SET_ERRORS", errors: newErrors });
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validate()) alert("Form submitted successfully!");
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Name:</label>
        <input
          type="text"
          value={state.name}
          onChange={(e) =>
            dispatch({ type: "SET_FIELD", field: "name", value: e.target.value })
          }
        />
        {state.errors.name && <small>{state.errors.name}</small>}
      </div>
      <div>
        <label>Email:</label>
        <input
          type="email"
          value={state.email}
          onChange={(e) =>
            dispatch({ type: "SET_FIELD", field: "email", value: e.target.value })
          }
        />
        {state.errors.email && <small>{state.errors.email}</small>}
      </div>
      <div>
        <label>Password:</label>
        <input
          type="password"
          value={state.password}
          onChange={(e) =>
            dispatch({ type: "SET_FIELD", field: "password", value: e.target.value })
          }
        />
        {state.errors.password && <small>{state.errors.password}</small>}
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default DynamicForm;
```

---

### **Approach 4: Form Validation with Libraries (Formik and Yup)**

```jsx
import React from "react";
import { useFormik } from "formik";
import * as Yup from "yup";

const DynamicForm = () => {
  const formik = useFormik({
    initialValues: { name: "", email: "", password: "" },
    validationSchema: Yup.object({
      name: Yup.string().required("Name is required."),
      email: Yup.string().email("Invalid email format.").required("Email is required."),
      password: Yup.string()
        .min(6, "Password must be at least 6 characters.")
        .required("Password is required."),
    }),
    onSubmit: (values) => {
      alert("Form submitted successfully!");
    },
  });

  return (
    <form onSubmit={formik.handleSubmit}>
      <div>
        <label>Name:</label>
        <input
          type="text"
          name="name"
          value={formik.values.name}
          onChange={formik.handleChange}
        />
        {formik.errors.name && <small>{formik.errors.name}</small>}
      </div>
      <div>
        <label>Email:</label>
        <input
          type="email"
          name="email"
          value={formik.values.email}
          onChange={formik.handleChange}
        />
        {formik.errors.email && <small>{formik.errors.email}</small>}
      </div>
      <div>
        <label>Password:</label>
        <input
          type="password"
          name="password"
          value={formik.values.password}
          onChange={formik.handleChange}
        />
        {formik.errors.password && <small>{formik.errors.password}</small>}
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default DynamicForm;
```

---

These approaches cover basic to advanced scenarios. Formik/Yup is highly recommended for robust validations. Let me know if you need deeper insights!