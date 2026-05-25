# LOGIC MÀN HÌNH CHUNG (COMMON SCREEN LOGIC - CS) - TEMPLATE

## Phân hệ [Tên Phân Hệ] | Hệ thống [Tên Hệ thống]

> Mô tả tóm tắt mục đích của tài liệu này (Ví dụ: Định nghĩa các quy tắc chung về giao diện và thao tác cho màn hình X).

---

## CS_XX: [Tên Cấu trúc Màn hình/Logic Chung]

> [Mô tả tổng quan về đối tượng áp dụng. Ví dụ: Áp dụng cho tất cả báo cáo định kỳ...]

### 1. Header / Tiêu đề màn hình

- **Quy tắc hiển thị:** [Mô tả cách tiêu đề hiển thị, ví dụ: lấy theo tên chức năng, động hay tĩnh...]

### 2. Bộ lọc (Filters) & Tìm kiếm (Search)

- **Các bộ lọc bắt buộc:**
  - [Tên Filter 1]: [Quy tắc, loại component (Dropdown/Checkbox/DatePicker...)]
  - [Tên Filter 2]: [Quy tắc...]
- **Thanh tìm kiếm (Search Bar):**
  - **Placeholder:** [Cú pháp placeholder, VD: "Tìm kiếm theo..."]
  - **Hành vi thực thi (Execution):** [Cần Enter hay tự động lọc khi nhập (Auto-filter)?]

### 3. Cấu trúc Hiển thị Danh sách (List/Grid/Group)

- **Trạng thái mặc định (Default State):** [Hiển thị phẳng (Flat) hay nhóm (Group/Accordion), mặc định đóng hay mở...]
- **Phân quyền/Đặc thù (Role-based Logic):** [Khác biệt khi user A xem so với user B, ví dụ: 1 phân hệ vs nhiều phân hệ]
- **Empty States (Trạng thái dữ liệu trống):** [Hiển thị message gì khi không có dữ liệu?]
- **Phân trang/Cuộn (Pagination/Scroll):** [Giới hạn bản ghi, có tải thêm (Load more) hay phân trang (Pagination)?]

### 4. Quy tắc UI/UX Đặc biệt (Nếu có)

- **Tương tác (Interaction):** [Click vào phần tử A thì điều gì xảy ra...]
- **Hiển thị biểu tượng/Tooltip:** [Khi nào hiển thị icon? Hover vào icon thì hiện tooltip gì?]
