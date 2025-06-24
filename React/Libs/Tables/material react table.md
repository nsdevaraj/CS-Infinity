

```jsx
import { useEffect, useMemo, useState } from "react";
import {
  MaterialReactTable,
  useMaterialReactTable,
  type MRT_ColumnDef,
} from "material-react-table";
import { Box, Typography } from "@mui/material";

interface Product {
  id: number;
  title: string;
  price: number;
}

export default function MRT_Table() {
  const [data, setData] = useState<Product[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [rowCount, setRowCount] = useState(0);
  const [pagination, setPagination] = useState({
    pageIndex: 0,
    pageSize: 2,
  });

  const columns = useMemo<MRT_ColumnDef<Product>[]>(
    () => [
      { accessorKey: "id", header: "ID", size: 80 },
      { accessorKey: "title", header: "Title", size: 300 },
      {
        accessorKey: "price",
        header: "Price ($)",
        size: 100,
        Cell: ({ cell }) => `$${cell.getValue<number>().toFixed(2)}`,
      },
    ],
    []
  );

  const fetchPage = async (pageIndex: number, pageSize: number) => {
    setIsLoading(true);
    try {
      const offset = pageIndex * pageSize;
      const res = await fetch(
        `https://api.escuelajs.co/api/v1/products?offset=${offset}&limit=${pageSize}`
      );
      const items: Product[] = await res.json();

      setData(items);
      setRowCount(200);
    } catch (err) {
      console.error("Failed to fetch products:", err);
    } finally {
      setIsLoading(false);
    }
  };

  useEffect(() => {
    fetchPage(pagination.pageIndex, pagination.pageSize);
  }, [pagination.pageIndex, pagination.pageSize]);

  const table = useMaterialReactTable({
    columns,
    data,
    state: {
      isLoading,
      pagination,
      showProgressBars: isLoading,
    },
    onPaginationChange: setPagination,
    rowCount,
    manualPagination: true, // tells MRT we're controlling paging
    muiTableContainerProps: { sx: { maxHeight: "5000px" } },
  });

  return (
    <Box>
      <MaterialReactTable table={table} />
      <Typography variant="caption" sx={{ p: 2 }}>
        Fetched page: {pagination.pageIndex + 1}
      </Typography>
    </Box>
  );
}

```


