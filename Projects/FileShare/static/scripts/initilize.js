"use strict";

function initialize() {
    const settings = allData();
    settings.forEach(variable => {
        const value = localStorage.getItem(variable);
        if (variable.startsWith("--")) {
            changeVariable(variable, value);
        }
    });
}

function allData() {
    return Object.keys(localStorage);
}

function changeVariable(variable, value) {
    const root = document.documentElement;
    root.style.setProperty(variable, value);
}

initialize();