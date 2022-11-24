export type NavItem = {
    name: string,
    urlPath: string,
};

export interface NavItemList {
    [details: string]: NavItem[]
}

const navItems: NavItemList = {
    imaging: [
        {
            name: "Mathematical Transform",
            urlPath: "math-transform"
        },
        {
            name: "Pixel Intensity Heatmap",
            urlPath: "heatmap"
        },
        {
            name: "Smooth Image (Convolutional)",
            urlPath: "smooth-conv"
        },
        {
            name: "Object Extraction",
            urlPath: "object-extraction"
        }
    ],
    data: [
    ]
};

export default navItems;
