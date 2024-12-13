
```jsx
import { useState } from "react";

export default function App() {
  const [activeNavItem, setActiveNavItem] = useState("Factory Summary");
  const [openAccordion, setOpenAccordion] = useState(null);

  const navPanelOptions = [
    "Factory Summary",
    "Version Approval",
    "ECU Submission"
  ];

  const handleAccordionToggle = (index) => {
    setOpenAccordion(openAccordion === index ? null : index);
  };

  const renderAccordions = () => {
    const accordionContent = [
      {
        title: "Sample HTML Accordion",
        content: (
          <p>This is a sample HTML content inside the accordion.</p>
        ),
      },
      {
        title: "Embedded Google Maps",
        content: (
          <iframe
            title="Google Maps"
            src="https://www.google.com/maps/embed"
            width="100%"
            height="200"
            style={{ border: 0 }}
            allowFullScreen=""
            loading="lazy"
          ></iframe>
        ),
      },
      {
        title: "Random Lorem Texts",
        content: (
          <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla ut
            sapien nec nulla feugiat tincidunt.
          </p>
        ),
      },
    ];

    return accordionContent.map((item, index) => (
      <div key={index}>
        <button
          className="accordion"
          onClick={() => handleAccordionToggle(index)}
        >
          {item.title}
        </button>
        <div
          className="panel"
          style={{
            maxHeight: openAccordion === index ? "200px" : "0",
            overflow: "hidden",
            transition: "max-height 0.3s ease-out",
          }}
        >
          {item.content}
        </div>
      </div>
    ));
  };

  const itemRenderer = (item) => {
    const optionStyles = {
      color: "white",
      backgroundColor: "#C9B2A0",
      cursor: "pointer",
      padding: "10px",
      margin: "5px 0",
      textAlign: "center",
      fontWeight: activeNavItem === item ? "bold" : "normal",
      border: activeNavItem === item ? "5px solid #F4EBDC" : "none",
    };

    return (
      <div
        key={item}
        style={optionStyles}
        onClick={() => setActiveNavItem(item)}
      >
        {item}
      </div>
    );
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "row",
        fontWeight: "bold",
        boxSizing: "border-box",
        backgroundImage: `url("https://plus.unsplash.com/premium_photo-1666700698920-d2d2bba589f8?q=80&w=1632&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")`,
        backgroundSize: "cover",
        backgroundPosition: "center",
        height: "100vh",
        color: "#333",
      }}
    >

      <div
        style={{
          width: "200px",
          height: "100vh",
          backdropFilter: "blur(10px)",
          backgroundColor: "rgba(255, 255, 255, 0.7)",
          padding: "10px",
        }}
      >
        {navPanelOptions.map((item) => itemRenderer(item))}
      </div>

      <div
        style={{
          flex: 1,
          padding: "20px",
          overflowY: "auto",
          backgroundColor: "rgba(255, 255, 255, 0.9)",
        }}
      >
        <h2>{activeNavItem}</h2>
        {renderAccordions()}
      </div>
    </div>
  );
}

```

