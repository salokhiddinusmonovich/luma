// src/routes/index.tsx

import { createBrowserRouter, RouteObject } from "react-router-dom";
import MainLayout from "@/layout/MainLayout";
import Index from "@/pages/Index";
import NotFoundPage from "@/pages/error/NotFoundPage";

export const routes: RouteObject[] = [
    {
        path: "/",
        element: <MainLayout />,
        errorElement: <NotFoundPage />,
        children: [
            {
                index: true,
                element: <Index />,
            },
        ],
    },
];

export const router = createBrowserRouter(routes);
