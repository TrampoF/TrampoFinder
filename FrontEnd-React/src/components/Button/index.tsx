import React, { useState } from "react";
import styled from "styled-components";

const SelectedButton = styled.div`
    cursor: pointer;
    user-select: none;
    padding: 4px 8px;
    margin: auto auto;
    background-color: var(--grey);
    color: var(--black);
    border-radius: 8px;
`;

const DefaultButton = styled(SelectedButton)`
    background-color: var(--tertiary-color);
    color: var(--on-tertiary-color);
`

interface ButtonProps {
    name: string
}

const Button: React.FC<ButtonProps> = ({ name }) => {
    const [isSelected, setIsSelected] = useState(false);

    const handleClick = (): void => setIsSelected(!isSelected);

    return isSelected ? <DefaultButton onClick={handleClick}>{name}</DefaultButton>
        : <SelectedButton onClick={handleClick}>{name}</SelectedButton>;
}

export default Button;