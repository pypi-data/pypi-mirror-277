// ipyantd/assets/antd-jupyter.tsx
import * as React from "react";
import * as antd from "antd";
function SliderStatefull({ value, setValue, ...rest }) {
  return /* @__PURE__ */ React.createElement(antd.Slider, { value, onChange: (v) => setValue(v), ...rest });
}
function SelectStatefull({ value, setValue, ...rest }) {
  return /* @__PURE__ */ React.createElement(antd.Select, { value, onChange: (v) => setValue(v), ...rest });
}
function SwitchStatefull({ value, setValue, ...rest }) {
  return /* @__PURE__ */ React.createElement(antd.Switch, { value, onChange: (v) => setValue(v), ...rest });
}
function DropdownStatefull({ value, setValue, ...rest }) {
  const onOpenChange = (open, info) => {
    setValue(open);
    if (rest.onOpenChange) {
      rest.onOpenChange({ open, info });
    }
  };
  return /* @__PURE__ */ React.createElement(antd.Dropdown, { open: value, onOpenChange, ...rest });
}
function ModalStatefull({ value, setValue, ...rest }) {
  const onOpenChange = (open) => {
    setValue(open);
    if (rest.onOpenChange) {
      rest.afterOpenChange(open);
    }
  };
  const handleOk = () => {
    if (rest.onOk) {
      rest.onOk();
    }
  };
  const handleCancel = () => {
    if (rest.onCancel) {
      rest.onCancel();
    }
  };
  return /* @__PURE__ */ React.createElement(antd.Modal, { open: value, afterOpenChange: onOpenChange, onOk: handleOk, onCancel: handleCancel, ...rest });
}
export {
  DropdownStatefull,
  ModalStatefull,
  SelectStatefull,
  SliderStatefull,
  SwitchStatefull
};
