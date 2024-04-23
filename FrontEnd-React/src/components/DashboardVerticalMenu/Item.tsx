import React, { useState } from "react";
import styled from "styled-components";

const SelectedItem = styled.div`
    cursor: pointer;
    user-select: none;
    padding: 8px 12px;
    margin: auto auto;
    background-color: var(--grey);
    color: var(--black);
    border-radius: 8px;
`;

const DefaultItem = styled(SelectedItem)`
    background-color: var(--tertiary-color);
    color: var(--on-tertiary-color);
`

interface ItemProps {
    name: string
}

const Item: React.FC<ItemProps> = ({ name }) => {
    const [isSelected, setIsSelected] = useState(false);

    const handleClick = (): void => setIsSelected(!isSelected);

    return isSelected ? <DefaultItem onClick={handleClick}>{name}</DefaultItem>
        : <SelectedItem onClick={handleClick}>{name}</SelectedItem>;
}

export default Item;