# UC Readiness Review
**Functional / Black-box Test Readiness Template**

---

> **Tài liệu:** UC329-334 — Tình hình thu hồi quyết định chủ trương đầu tư/GCNĐKĐT tại các KCN, KKT trong kỳ báo cáo (SRS v1.5, 2026-05-18)
> **Ngày audit:** 2026-05-21
> **Người audit:** Antigravity QC Agent
> **Phiên bản:** v2

---

## Feature Brief

Chức năng cho phép Ban Quản lý các KCN, KKT lập và theo dõi báo cáo định kỳ (quý/năm) về tình hình thu hồi quyết định chủ trương đầu tư/GCNĐKĐT tại các KCN, KKT. Báo cáo thuộc mẫu biểu 2116.H.QLKKT, nộp cho Cục Đầu tư nước ngoài. Hệ thống hỗ trợ: xem danh sách báo cáo theo kỳ hạn, lập mới báo cáo (chọn dự án bị thu hồi, hệ thống tự động phân loại vào 2 mục theo loại hình dự án và auto-fill dữ liệu từ API), và các tác vụ bổ trợ (xem chi tiết, xem vòng đời, in, xuất báo cáo, nộp, chỉnh sửa, xóa). Đây là báo cáo đơn lẻ (single report form), giao diện Admin site, áp dụng luồng quy trình xử lý >2 bước (CMCĐT_BCTK_04).

---

## Readiness Verdict

| Overall Score | Verdict |
| ------------- | ------- |
| `99.1 / 100` | ✅ **READY** |

---

## 0. Document Metadata

| UC-ID | Feature Name | Version | Status |
|-------|-------------|---------|--------|
| UC329-334 | Tình hình thu hồi quyết định chủ trương ĐT/GCNĐKĐT tại các KCN, KKT | v1.5 | Approved |

| Author / BA | Approved By | Date Created | Last Updated |
|-------------|-------------|--------------|--------------|
| yen.trinh | — | 2026-04-23 | 2026-05-18 |

**Status:** ✅ Complete

---

## 1. Objective & Scope

### 1.1 Objective
Cho phép Ban Quản lý các KCN, KKT theo dõi và báo cáo tình hình thu hồi quyết định chủ trương đầu tư/GCNĐKĐT tại các KCN, KKT trong từng kỳ báo cáo (quý/năm), nộp cho Cục Đầu tư nước ngoài theo mẫu biểu 2116.H.QLKKT.

### 1.2 In Scope
- UC329-334.1: Xem danh sách báo cáo (nhóm theo kỳ hạn, lọc, tìm kiếm, expand/collapse kỳ hạn)
- UC329-334.2: Lập mới báo cáo (thêm nhiều dòng, chọn dự án, auto-fill song song từ API nội bộ + IRC, tự động phân loại Mục 1/Mục 2)
- UC329-334.3: Các tác vụ bổ trợ (Xem chi tiết, Xem vòng đời, In, Xuất báo cáo dưới định dạng .docx, Nộp, Chỉnh sửa, Xóa)

### 1.3 Out of Scope
- Nhập từ file (nút "Nhập từ file" hiển thị trên giao diện nhưng logic xử lý chi tiết tham chiếu CF_02)
- Quy trình phê duyệt/tiếp nhận phía cơ quan nhận (Cục Đầu tư nước ngoài)
- Quản lý dự án nội bộ và Cổng 1 cửa QG (IRC) - là nguồn dữ liệu API cho hệ thống gọi tự động.

**Status:** ✅ Complete

---

## 2. Actors & Stakeholders

| Actor | Type | Role & Permissions |
|-------|------|-------------------|
| Ban Quản lý các KCN, KKT | Primary | Xem danh sách, Lập mới, Chỉnh sửa, Nộp, Xóa, In, Xuất báo cáo. NĐT thành viên không có quyền truy cập báo cáo này (Báo cáo chỉ dành cho Admin site). Phân quyền 1 role duy nhất. Tham chiếu: CMR_01, CMR_04 |
| Hệ thống (API nội bộ + API IRC) | System | Cung cấp dữ liệu dự án, auto-fill các trường thông tin, phân loại dự án |
| Cục Đầu tư nước ngoài | External | Cơ quan nhận báo cáo |

**Status:** ✅ Complete

---

## 3. Preconditions & Postconditions

### 3.1 Preconditions
- Người dùng đã đăng nhập với vai trò Ban Quản lý các KCN, KKT
- Người dùng truy cập: Phân hệ Báo cáo → Báo cáo KKT/KCN → Tình hình thu hồi quyết định chủ trương ĐT/GCNĐKĐT tại các KCN, KKT
- Kỳ hạn báo cáo ở trạng thái "Trong thời hạn" (đối với chức năng Lập báo cáo / Nhập từ file). Tham chiếu: CMR_04
- Hệ thống API Quản lý dự án nội bộ và API IRC (Cổng 1 cửa QG) khả dụng (đối với chức năng Lập báo cáo)

### 3.2 Postconditions
| After completing... | System state / Postcondition |
|--------------------|------------------------------|
| Lập báo cáo + Lưu nháp | Bản ghi mới ở trạng thái "Lưu nháp" xuất hiện trong danh sách kỳ tương ứng. Mã báo cáo được sinh theo quy tắc `EZ_2116HQLKKT_[ID]` (Global Unique). Toast thành công: `"Đã lập báo cáo thành công"` (T01). |
| Lập báo cáo + Nộp | Bản ghi chuyển sang trạng thái "Chờ duyệt" (do loại quy trình >2 bước). Toast thành công: `"Đã nộp báo cáo thành công"` (T02). Quy trình workflow `CMCĐT_BCTK_04` tiếp theo được trigger. |
| Chỉnh sửa + Lưu nháp | Dữ liệu bản ghi được cập nhật trong DB, trạng thái bản ghi được bảo toàn (Lưu nháp giữ nguyên Lưu nháp, YCCS giữ nguyên YCCS). Ngày cập nhật thay đổi. Toast thành công: `"Đã chỉnh sửa báo cáo thành công"` (T03). |
| Xóa báo cáo | Bản ghi bị xóa vĩnh viễn khỏi DB và biến mất khỏi danh sách. Toast thành công: `"Xóa báo cáo thành công"` (T08). |

**Status:** ✅ Complete

---

## 4. UI Object Inventory & Mapping

### Màn hình Danh sách (UC329-334.1)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 1 | Danh sách > Bộ lọc | Năm | YearPicker | No | Null | "Chọn năm" | Toàn bộ các năm khả dụng | Lọc danh sách theo năm báo cáo. Kết quả lọc hiển thị ngay. Tham chiếu: CMR_07, CS_01 Mục 2 | UC 329-334_ManHinhDanhSach.png |
| 2 | Danh sách > Bộ lọc | Trạng thái | Multiple-selection Dropdown | No | "Tất cả trạng thái" | "Chọn trạng thái" | Tất cả trạng thái / Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | Lọc theo trạng thái của báo cáo. Kết quả lọc hiển thị ngay. Tham chiếu: CMR_03, CMR_07, CMR_16 | UC 329-334_ManHinhDanhSach.png |
| 3 | Danh sách > Bộ lọc | Mã báo cáo | Search bar | No | Null | "Tìm kiếm nhanh theo mã báo cáo" | N/A | Tìm kiếm theo mã báo cáo, kết quả hiển thị ngay (real-time). Tham chiếu: CMR_06, CMR_09 | UC 329-334_ManHinhDanhSach.png |
| 4 | Danh sách > Bộ lọc | Trạng thái kỳ | Multiple-selection Dropdown | No | Null | "Chọn trạng thái kỳ" | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | Lọc theo trạng thái kỳ. Kết quả lọc hiển thị ngay. Tham chiếu: CMR_04, CMR_16 | UC 329-334_ManHinhDanhSach.png |
| 5 | Danh sách > Bộ lọc | Năm | Yearpicker | No | Null | "Chọn năm" | Toàn bộ các năm khả dụng | Lọc danh sách theo năm báo cáo. Kết quả lọc hiển thị ngay. Tham chiếu: CMR_07, CS_01 Mục 2 | UC 329-334_ManHinhDanhSach.png |
| 6 | Danh sách > Khung Kỳ hạn | Kỳ hạn báo cáo | Label (collapsible header) | N/A | Collapse | — | N/A | Hiển thị tên kỳ hạn, mặc định collapse, click mũi tên expand. Tham chiếu: CMR_08 | UC 329-334_ManHinhDanhSach.png |
| 7 | Danh sách > Khung Kỳ hạn | Trạng thái kỳ báo cáo | Label (status chip) | N/A | — | — | Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | Hiển thị trạng thái kỳ theo thời gian. Tham chiếu: CMR_04 | UC 329-334_ManHinhDanhSach.png |
| 8 | Danh sách > Khung Kỳ hạn | Lập báo cáo | Button | N/A | — | — | N/A | Chỉ hiển thị khi kỳ "Trong thời hạn". Ẩn khi "Chưa tới hạn" hoặc "Qua kỳ báo cáo". Tham chiếu: CF_01, CMR_04 | UC 329-334_ManHinhDanhSach.png |
| 9 | Danh sách > Khung Kỳ hạn | Nhập từ file | Button | N/A | — | — | N/A | Chỉ hiển thị khi kỳ "Trong thời hạn". Ẩn khi "Chưa tới hạn" hoặc "Qua kỳ báo cáo". Tham chiếu: CF_02, CMR_04 | UC 329-334_ManHinhDanhSach.png |
| 10 | Danh sách > Bảng BC | Mã báo cáo | Label (table column) | N/A | — | — | N/A | Mã báo cáo sinh theo quy tắc `EZ_2116HQLKKT_[ID]`. Tham chiếu: CMR_09 | UC 329-334_ManHinhDanhSach.png |
| 11 | Danh sách > Bảng BC | Ngày cập nhật | Label (table column) | N/A | — | — | N/A | Định dạng: dd/MM/yyyy HH:mm | UC 329-334_ManHinhDanhSach.png |
| 12 | Danh sách > Bảng BC | Trạng thái | Label (table column) | N/A | — | — | Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | Trạng thái bản ghi. Tham chiếu: CMR_03 | UC 329-334_ManHinhDanhSach.png |
| 13 | Danh sách > Bảng BC | Hành động | Button group (table column) | N/A | — | — | N/A | Hiển thị các nút thao tác theo trạng thái. Tham chiếu: UC329-334.3 | UC 329-334_ManHinhDanhSach.png |
| 14 | Danh sách > Phân trang | Phân trang | Pagination control | N/A | 10 bản ghi/trang | — | 10 / 20 / 50 / 100 | Phân trang theo kỳ. Tham chiếu: CMR_10 | UC 329-334_ManHinhDanhSach.png |
| 15 | Danh sách > Empty state | "Không tìm thấy kết quả" | Empty state message | N/A | — | — | N/A | Hiển thị khi không có kết quả tìm kiếm/lọc | UC 329-334_ManHinhDanhSach.png |

### Màn hình Lập Báo Cáo (UC329-334.2)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 16 | Lập BC > Mục 1 Header | MỤC 1 – DỰ ÁN ĐẦU TƯ XÂY DỰNG VÀ KINH DOANH KẾT CẤU HẠ TẦNG KCN, KKT | Section header | N/A | — | — | N/A | Hệ thống tự phân loại bản ghi vào mục này nếu dự án thuộc loại hình đầu tư xây dựng và kinh doanh hạ tầng theo API | UC 329-334_ManHinhLapBaoCao.png |
| 17 | Lập BC > Mục 2 Header | MỤC 2 – DỰ ÁN ĐẦU TƯ SẢN XUẤT KINH DOANH TRONG KCN, KKT | Section header | N/A | — | — | N/A | Hệ thống tự phân loại bản ghi vào mục này nếu dự án thuộc loại hình đầu tư sản xuất kinh doanh theo API | UC 329-334_ManHinhLapBaoCao.png |
| 18 | Lập BC > Bảng > Cột 1 | STT | Label (auto-increment) | N/A | Tự tăng | — | N/A | Số thứ tự tự động tăng theo từng dòng trong mỗi mục, bắt đầu từ 1 | UC 329-334_ManHinhLapBaoCao.png |
| 19 | Lập BC > Bảng > Cột 2 | Tên dự án đầu tư | Dropdown (Searchable) | Yes | Null | "Chọn tên dự án đầu tư" | Danh sách dự án từ API Quản lý dự án nội bộ | Khi chọn, gọi song song 2 API (nội bộ + IRC) để auto-fill cột 3–8 và phân loại Mục 1/2. Tham chiếu: CF_01, CMR_04, CMR_07 | UC 329-334_ManHinhLapBaoCao.png |
| 20 | Lập BC > Bảng > Cột 3 | KCN/KKT | Textbox (Disabled) | Yes | Từ API | — | N/A | Tự động điền từ API nội bộ. Trạng thái: Disabled. Tham chiếu: CMR_12 | UC 329-334_ManHinhLapBaoCao.png |
| 21 | Lập BC > Bảng > Cột 4 | Văn bản thành lập hoặc tương đương | Textbox (Disabled) | Yes | Từ API | — | N/A | Tự động điền từ API nội bộ. Trạng thái: Disabled. Tham chiếu: CMR_12 | UC 329-334_ManHinhLapBaoCao.png |
| 22 | Lập BC > Bảng > Cột 5 | Nhà đầu tư | Textbox (Disabled) | Yes | Từ API | — | N/A | Tự động điền từ API nội bộ. Nhiều NĐT ngăn cách bằng dấu phẩy. Trạng thái: Disabled. Tham chiếu: CMR_12 | UC 329-334_ManHinhLapBaoCao.png |
| 23 | Lập BC > Bảng > Cột 6 | Quốc tịch nhà đầu tư | Textbox (Disabled) | Yes | Từ API | — | N/A | Tự động điền từ API nội bộ. Hiển thị tương ứng danh sách NĐT cột 5. Trạng thái: Disabled. Tham chiếu: CMR_12 | UC 329-334_ManHinhLapBaoCao.png |
| 24 | Lập BC > Bảng > Cột 7 | Vốn đầu tư đã đăng ký – Vốn ĐTNN (tr. USD) | Textbox (Disabled) | Yes | Từ IRC | — | N/A | Tự động điền từ API IRC. Trạng thái: Disabled. Tham chiếu: CMR_12 | UC 329-334_ManHinhLapBaoCao.png |
| 25 | Lập BC > Bảng > Cột 8 | Vốn đầu tư đã đăng ký – Vốn ĐTTN (tỷ VNĐ) | Textbox (Disabled) | Yes | Từ IRC | — | N/A | Tự động điền từ API IRC. Trạng thái: Disabled. Tham chiếu: CMR_12 | UC 329-334_ManHinhLapBaoCao.png |
| 26 | Lập BC > Bảng > Cột 9 | Văn bản thu hồi chủ trương ĐT/GCNĐKĐT | Textbox | Yes | Null | "Nhập Văn bản thu hồi chủ trương ĐT/GCNĐKĐT" | N/A | Nhập tay. Validate bắt buộc khi Lưu nháp/Nộp. Tham chiếu: CMR_06 | UC 329-334_ManHinhLapBaoCao.png |
| 27 | Lập BC > Bảng > Cột 10 | Hành động | Icon button | N/A | — | — | N/A | Icon Xóa dòng (🗑️ hoặc ✕). Chỉ hiển thị khi bảng có từ 2 dòng trở lên. Tham chiếu: CMR_15 | UC 329-334_ManHinhLapBaoCao.png |
| 28 | Lập BC > Dòng cuối Mục 1 | Thêm dòng mục DA ĐT & KD kết cấu hạ tầng KCN, KKT | Button | N/A | — | — | N/A | Thêm 1 dòng trống mới vào cuối Mục 1. Luôn enabled. Tham chiếu: CMR_15 | UC 329-334_ManHinhLapBaoCao.png |
| 29 | Lập BC > Dòng cuối Mục 2 | Thêm dòng mục dự án SXKD trong KCN, KKT | Button | N/A | — | — | N/A | Thêm 1 dòng trống mới vào cuối Mục 2. Luôn enabled. Tham chiếu: CMR_15 | UC 329-334_ManHinhLapBaoCao.png |
| 30 | Lập BC > Footer | Hủy | Button | N/A | — | — | N/A | Tham chiếu: CF_01 (mục "Xử lý nút [Hủy]"), CMR_14 | UC 329-334_ManHinhLapBaoCao.png |
| 31 | Lập BC > Footer | Xem trước | Button | N/A | — | — | N/A | Xem trước báo cáo dưới dạng biểu mẫu. Tham chiếu: CF_07.1 | UC 329-334_ManHinhLapBaoCao.png |
| 32 | Lập BC > Footer | Lưu nháp | Button | N/A | — | — | N/A | Lưu nháp dữ liệu báo cáo. Tham chiếu: CF_01, CMR_14 | UC 329-334_ManHinhLapBaoCao.png |
| 33 | Lập BC > Footer | Nộp báo cáo | Button | N/A | — | — | N/A | Nộp báo cáo lên Cục Đầu tư nước ngoài. Tham chiếu: CF_01, CMR_14 | UC 329-334_ManHinhLapBaoCao.png |

### Màn hình Xem chi tiết & Tác vụ bổ trợ (UC329-334.3)

| # | Screen / Section | Label (verbatim) | Type | Required | Default | Placeholder | Enum values | Description / Constraint | Source |
|---|------------------|------------------|------|----------|---------|-------------|-------------|--------------------------|--------|
| 34 | Xem chi tiết > Form | (Toàn bộ trường giống Lập BC) | Form read-only | N/A | — | — | N/A | Layout giống hệt màn hình Lập BC, toàn bộ Disabled. Tham chiếu: CF_07 | — |
| 35 | Xem chi tiết > Footer | Chỉnh sửa | Button | N/A | — | — | N/A | Chỉ hiển thị khi trạng thái Lưu nháp hoặc YCCS. Tham chiếu: CF_07, CMR_03 | — |
| 36 | Xem chi tiết > Footer | Hủy | Button | N/A | — | — | N/A | Quay về Danh sách, không cần popup xác nhận | — |
| 37 | Hành động > Danh sách | Nộp | Button | N/A | — | — | N/A | Chỉ khi trạng thái Lưu nháp. Phân quyền: Người tạo. Tham chiếu: CF_09, CF_01 | — |
| 38 | Hành động > Danh sách | Chỉnh sửa | Button | N/A | — | — | N/A | Chỉ khi trạng thái YCCS và Lưu nháp. Phân quyền: Người tạo. Tham chiếu: CF_03 | — |
| 39 | Hành động > Danh sách | Xem chi tiết | Button | N/A | — | — | N/A | Luôn hiển thị (Tất cả trạng thái). Tất cả người dùng. Tham chiếu: CF_07 | — |
| 40 | Hành động > Danh sách | Xem vòng đời | Button | N/A | — | — | N/A | Luôn hiển thị (Tất cả trạng thái). Tất cả người dùng. Tham chiếu: CF_06 | — |
| 41 | Hành động > Danh sách | In | Button | N/A | — | — | N/A | Luôn hiển thị (Tất cả trạng thái). Mở màn hình In PDF. Tham chiếu: CF_05 | — |
| 42 | Hành động > Danh sách | Xuất báo cáo | Button | N/A | — | — | N/A | Luôn hiển thị (Tất cả trạng thái). Tất cả người dùng. Định dạng Docx. Tham chiếu: CF_04 | — |
| 43 | Hành động > Danh sách | Xóa | Button | N/A | — | — | N/A | Chỉ khi Lưu nháp VÀ chưa từng nộp. Phân quyền: Người tạo. Tham chiếu: CF_08 | — |

**Status:** ✅ Complete

---

## 5. Object Attributes & Behavior Definition

| # | Object / Component | System States | Interaction Matrix | Object Behavior (Data/State Change Context) |
|---|---|---|---|---|
| 1 | Năm / Năm (Dropdown filters #1 & #5) | Enabled. Mặc định: Null | Click: Mở YearPicker. Chọn năm: Đóng dropdown, lọc ngay lập tức | Khi thay đổi giá trị lọc → danh sách kỳ hạn bên dưới cập nhật ngay, không cần nút xác nhận. Năm không có dữ liệu hiển thị Empty State. Tham chiếu: CS_01 Mục 2 |
| 2 | Trạng thái (Multiple-selection filter #2) | Enabled. Mặc định: "Tất cả trạng thái" (CMR_16) | Click: Mở danh sách checkbox. Chọn/bỏ chọn các trạng thái: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa | Khi chọn/bỏ chọn → danh sách báo cáo cập nhật ngay (real-time). Khi bỏ chọn hết → hiển thị mặc định "Tất cả trạng thái" và hiển thị toàn bộ bản ghi. Tham chiếu: CMR_16 |
| 3 | Mã báo cáo (Search bar filter #3) | Enabled. Mặc định: Null | Nhập chữ/số: Lọc kết quả ngay khi người dùng gõ từng ký tự (real-time). Case-insensitive & partial match. Auto-trim khi call API | Tìm kiếm so khớp mã báo cáo. Nếu không tìm thấy kết quả → hiển thị Empty state: `"Không tìm thấy kết quả"` (CS_01). Placeholder: `"Tìm kiếm nhanh theo mã báo cáo"`. Max length: 500 ký tự. Tham chiếu: CMR_06, CMR_09 |
| 4 | Trạng thái kỳ (Multiple-selection filter #4) | Enabled. Mặc định: Null | Click: Mở danh sách checkbox. Chọn/bỏ chọn: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo | Khi thay đổi → danh sách kỳ hạn cập nhật ngay (real-time). Tách biệt với bộ lọc trạng thái bản ghi. Tham chiếu: CMR_04, CMR_16 |
| 5 | Kỳ hạn báo cáo (Collapsible header) | Mặc định: Collapse | Click vào vùng header hoặc mũi tên: Expand/Collapse | Expand → hiển thị danh sách các bản ghi báo cáo đã lập của kỳ đó, sắp xếp theo thứ tự mới → cũ. Collapse → thu gọn ẩn danh sách. Tham chiếu: CMR_08 |
| 6 | Trạng thái kỳ báo cáo (Label chip) | Read-only. Trạng thái dựa trên realtime so với kỳ hạn | N/A (hiển thị) | Tự động hiển thị theo thời gian thực tế: Chưa tới hạn / Trong thời hạn / Qua kỳ báo cáo. Tham chiếu: CMR_04 |
| 7 | Nút [Lập báo cáo] (Kỳ hạn) | Visible khi kỳ "Trong thời hạn". Ẩn (Hidden) khi "Chưa tới hạn" hoặc "Qua kỳ báo cáo" | Click: Điều hướng sang màn hình Lập báo cáo (UC329-334.2) | Cho phép người dùng khởi tạo 1 bản ghi mới của kỳ. Màn hình mở ra có sẵn 1 dòng trống mặc định. Tham chiếu: CF_01, CMR_04 |
| 8 | Nút [Nhập từ file] (Kỳ hạn) | Visible khi kỳ "Trong thời hạn". Ẩn (Hidden) khi "Chưa tới hạn" hoặc "Qua kỳ báo cáo" | Click: Mở popup Import file | Tham chiếu logic chi tiết tại CF_02. Tham chiếu: CMR_04 |
| 9 | Mã báo cáo (Bảng BC) | Read-only. Global Unique | N/A (hiển thị) | Sinh tự động khi bản ghi được tạo (Lưu nháp/Nộp). Quy tắc sinh mã: `EZ_2116HQLKKT_[ID]` (EZ là phân hệ Quản lý KCN, KKT; [ID] là định danh tự tăng). Tham chiếu: CMR_09 |
| 10 | Ngày cập nhật (Bảng BC) | Read-only | N/A (hiển thị) | Hiển thị ngày giờ thao tác gần nhất (Lưu nháp / Nộp). Định dạng hiển thị: dd/MM/yyyy HH:mm |
| 11 | Trạng thái (Bảng BC) | Read-only | N/A (hiển thị) | Hiển thị trạng thái hiện tại của bản ghi: Lưu nháp / Chờ duyệt / Đã tiếp nhận / Yêu cầu chỉnh sửa. Tham chiếu: CMR_03 |
| 12 | Hành động (Button group bảng BC) | Hiển thị các nút tương ứng với trạng thái bản ghi và quyền | Click từng nút hành động để trigger tác vụ | Điều kiện hiển thị và mapping hành động theo CMR_03. Chi tiết tại UC329-334.3 |
| 13 | Phân trang | Enabled. Mặc định: 10 bản ghi/trang | Click số trang hoặc nút Trang trước/Trang sau. Đổi dropdown số dòng/trang (10, 20, 50, 100) | Thanh phân trang cố định ở cuối danh sách. Trang 1 → nút [Trang trước] bị Disabled. Trang cuối → nút [Trang sau] bị Disabled. Đổi dropdown dòng/trang → reload grid quay về trang 1. Tham chiếu: CMR_10 |
| 14 | Empty state message | Visible khi kết quả lọc/tìm kiếm rỗng | N/A (hiển thị) | Hiển thị text `"Không tìm thấy kết quả"` ở vùng danh sách. Tham chiếu: CS_01 |
| 15 | Tên dự án đầu tư (Bảng Lập BC - Cột 2) | Enabled. Mặc định: Null. Trường bắt buộc | Click: Hiển thị dropdown chứa danh sách dự án lấy từ API. Nhập chữ: Lọc tìm kiếm tức thời (Instant Search) | Khi người dùng chọn 1 dự án → Hệ thống gọi song song 2 API (nội bộ + IRC) để điền tự động dữ liệu cột 3-8 và đọc thuộc tính loại hình dự án để tự phân loại bản ghi dồn vào Mục 1 hoặc Mục 2. Nếu bỏ trống khi Lưu nháp/Nộp → lỗi inline đỏ: `"Vui lòng chọn tên dự án đầu tư"` (V01). Tham chiếu: CF_01, CMR_04, CMR_07, CMR_12 |
| 16 | Các cột dữ liệu API (Cột 3, 4, 5, 6, 7, 8) | Disabled trước khi chọn dự án ở cột 2. Khi có dữ liệu API → Disabled. Khi API null hoặc API lỗi → Enabled | N/A khi Disabled. Click nhập liệu thủ công khi Enabled | Tự động điền dữ liệu từ API Quản lý dự án nội bộ (Cột 3: KCN/KKT, Cột 4: Văn bản thành lập, Cột 5: Nhà đầu tư - nhiều NĐT cách nhau dấu phẩy, Cột 6: Quốc tịch) và API IRC (Cột 7: Vốn ĐTNN - tr. USD, Cột 8: Vốn ĐTTN - tỷ VNĐ). Nếu API rỗng hoặc gọi thất bại (timeout/server error) → hiển thị Toast lỗi `"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."` (T05) và chuyển trường sang Enabled cho người dùng tự nhập tay. Trường bắt buộc trống → báo lỗi inline `"Vui lòng nhập [tên trường]"` (V01). Max length trường text = 500 ký tự. Max length trường số = 18 ký tự. Tham chiếu: CMR_05, CMR_06, CMR_12 |
| 17 | Văn bản thu hồi chủ trương ĐT/GCNĐKĐT (Cột 9) | Enabled. Mặc định: Null. Trường bắt buộc nhập tay duy nhất | Click: Focus trường. Nhập ký tự: Tự động uppercase (CMR_13). Nhập số công văn | Validate định dạng Số công văn theo chuẩn `[Số thứ tự]/[Ký hiệu 1]-[Ký hiệu 2]`. Auto-correct số thứ tự <10 (thêm `0` ở đầu). Chặn khoảng trắng và ký tự lạ ngoài `/` và `-`. Bắt buộc nhập khi cả Lưu nháp và Nộp. Nếu trống → lỗi inline đỏ: `"Vui lòng nhập Văn bản thu hồi chủ trương ĐT/GCNĐKĐT"` (V01). Sai format thiếu `/` → lỗi `"Số công văn chưa đúng chuẩn, thiếu dấu "/""` (V05). Thiếu `-` → lỗi `"Số công văn chưa đúng chuẩn, thiếu dấu "-""` (V06). Sai format tổng thể → lỗi `"Vui lòng nhập lại thông tin"` (V07). Max length = 500 ký tự. Tham chiếu: CMR_06, CMR_13 |
| 18 | Nút [Xóa dòng] (Cột 10) | Icon button. Chỉ hiển thị khi bảng (trong từng mục) có từ 2 dòng trở lên | Click: Xóa dòng ngay lập tức | Xóa dòng ngay mà không hiển thị popup xác nhận. Khi chỉ còn 1 dòng duy nhất trong mục → ẩn nút Xóa dòng. Tham chiếu: CMR_15 |
| 19 | Nút [Thêm dòng...] (Dòng cuối Mục 1 & 2) | Button ở footer mỗi Section bảng. Luôn enabled | Click: Thêm 1 dòng trống mới vào cuối bảng tương ứng | Thêm dòng trống. Các trường cột 3-8 ở dòng mới mặc định Disabled chờ chọn dự án ở cột 2. Không giới hạn số dòng (nhưng nếu vượt 500 dòng khi Nộp → Toast lỗi T16). Tham chiếu: CMR_15 |
| 20 | Nút [Hủy] (Form Lập BC) | Enabled (Tất cả trạng thái) | Click: Điều hướng quay về màn hình Danh sách | Áp dụng Dirty Form Guard: Nếu form có thay đổi (dirty) → hiển thị popup xác nhận rời trang `"Dữ liệu chưa được lưu / Bạn có chắc chắn muốn rời khỏi trang này không?"` (P02). Đồng ý → quay về danh sách và hủy dữ liệu in-memory. Hủy → đóng popup, ở lại form. Nếu form không dirty → quay về danh sách ngay không hiện popup. Tham chiếu: CF_01, CMR_14 |
| 21 | Nút [Xem trước] (Form Lập BC) | Enabled (Tất cả trạng thái) | Click: Mở màn hình/popup Xem trước báo cáo | Hiển thị trước giao diện kết xuất báo cáo. Tham chiếu: CF_07.1 |
| 22 | Nút [Lưu nháp] (Form Lập/Sửa) | Ở trạng thái Lưu nháp: Luôn Enabled. Ở trạng thái YCCS: Disabled khi form chưa dirty, Enabled ngay khi form dirty | Click: Thực hiện validate và lưu nháp dữ liệu | Khi ở trạng thái YCCS, nếu form chưa dirty thì nút bị Disabled, hover hiện tooltip: `"Vui lòng chỉnh sửa ít nhất một trường thông tin trước khi lưu nháp."`. Khi click thành công → Lưu dữ liệu → Toast thành công T01 (lập) hoặc T03 (chỉnh sửa). Bảo toàn trạng thái bản ghi. Tham chiếu: CF_01, CF_03, CMR_14 |
| 23 | Nút [Nộp báo cáo] (Form Lập/Sửa) | Ở trạng thái Lưu nháp: Luôn Enabled. Ở trạng thái YCCS: Disabled khi form chưa dirty, Enabled ngay khi form dirty | Click: Thực hiện validate toàn bộ form → popup xác nhận nộp P01 | Khi ở trạng thái YCCS, nếu form chưa dirty thì nút bị Disabled, hover hiện tooltip: `"Vui lòng chỉnh sửa ít nhất một trường thông tin trước khi nộp."`. Khi click thành công → kiểm tra validate: Nếu pass → mở popup xác nhận P01. Người dùng tích chọn checkbox xác nhận chính xác → Nút [Xác nhận] active → click [Xác nhận] → gửi API nộp → chuyển trạng thái "Chờ duyệt" → Toast thành công T02 → Điều hướng về màn hình Danh sách. Nếu không tích checkbox hoặc bấm [Hủy] trên popup → đóng popup, giữ nguyên form. Nếu validate rỗng/lỗi → hiển thị inline đỏ V01 dưới trường lỗi, dừng luồng. Tham chiếu: CF_01, CF_03, CMR_14, P01 |
| 24 | Màn hình Xem chi tiết (UC329-334.3) | Toàn bộ các trường dữ liệu ở trạng thái Disabled (Read-only) | Chỉ xem thông tin, không cho phép tương tác nhập liệu | Giao diện hiển thị giống hệt Lập báo cáo, phân chia 2 mục và điền sẵn dữ liệu. Tham chiếu: CF_07 |
| 25 | Nút [Chỉnh sửa] (Màn Xem chi tiết) | Chỉ hiển thị (Visible) khi bản ghi ở trạng thái Lưu nháp hoặc Yêu cầu chỉnh sửa. Ẩn khi Chờ duyệt/Đã tiếp nhận | Click: Điều hướng sang màn hình Chỉnh sửa (CF_03) | Mở form Chỉnh sửa, cho phép người dùng thay đổi dữ liệu của bản ghi. Tham chiếu: CF_07, CMR_03 |
| 26 | Nút [Hủy] (Màn Xem chi tiết) | Enabled (Tất cả trạng thái) | Click: Quay về màn hình Danh sách ngay | Không kích hoạt Dirty Form Guard vì màn hình chỉ xem (không bao giờ dirty), điều hướng quay về danh sách trực tiếp. |
| 27 | Các nút Hành động trên Danh sách (UC329-334.3) | Hiển thị động theo trạng thái của từng bản ghi | Click: Thực hiện tác vụ trực tiếp trên dòng | - **Trạng thái Lưu nháp:** Nộp (CF_09), Chỉnh sửa (CF_03), Xóa (CF_08 - chỉ khi chưa từng nộp), Xem chi tiết, Xem vòng đời, In, Xuất báo cáo. Nút Xóa ẩn vĩnh viễn nếu bản ghi đã từng nộp (Lifecycle Lock).
- **Trạng thái Chờ duyệt / Đã tiếp nhận:** Xem chi tiết, Xem vòng đời, In, Xuất báo cáo. (Khóa vĩnh viễn nút Sửa/Nộp/Xóa).
- **Trạng thái YCCS:** Chỉnh sửa, Xem chi tiết, Xem vòng đời, In, Xuất báo cáo. Nút Nộp hiển thị nhưng bị Disabled cho đến khi người dùng vào Chỉnh sửa, chỉnh ít nhất 1 trường và Lưu nháp thành công (CMR_14).
Tất cả người dùng đều có quyền In, Xem chi tiết, Xem vòng đời, Xuất báo cáo. Sửa/Xóa/Nộp chỉ dành cho Người tạo. Tham chiếu: CMR_03, CMR_14 |
| 28 | Phím tắt chuyển trường (Tab Navigation) | Enabled trên tất cả form nhập liệu | Nhấn Tab: Chuyển focus sang trường kế tiếp theo thứ tự từ trái qua phải, trên xuống dưới. Nhấn Shift+Tab: Chuyển focus ngược lại | Áp dụng cho các ô nhập liệu cột 2, cột 9 và các nút hành động trong form Lập/Sửa báo cáo. Tham chiếu: CMR_18 |

**Status:** ✅ Complete

---

## 6. Functional Logic & Workflow Decomposition

### 6.1 Function: Xem Danh Sách Báo Cáo (UC329-334.1)

#### A. Workflows

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | BQL KCN/KKT | Truy cập menu: Phân hệ Báo cáo → Báo cáo KKT/KCN → Tình hình thu hồi... | Hệ thống tải và hiển thị màn hình Danh sách với bộ lọc ở giá trị mặc định. Các kỳ hạn báo cáo ở trạng thái Collapse. | N/A | Lỗi kết nối API lấy danh sách → Hiển thị Toast lỗi hệ thống `"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."` (T05). |
| 2 | BQL KCN/KKT | Click mũi tên expand kỳ hạn báo cáo | Hệ thống hiển thị danh sách các báo cáo đã nộp/lưu nháp của kỳ đó, sắp xếp theo thứ tự mới → cũ (theo ngày cập nhật). | N/A | Kỳ hạn chưa có báo cáo nào được lập → expand ra hiển thị empty state tương ứng của kỳ hạn đó (theo CS_01). |
| 3 | BQL KCN/KKT | Chọn bộ lọc (Năm / Trạng thái / Trạng thái kỳ) hoặc nhập Mã BC | Hệ thống tự động lọc và hiển thị kết quả tương ứng ngay lập tức (real-time filtering), không cần nhấn thêm nút tìm kiếm. | Kết hợp đồng thời nhiều bộ lọc để thu hẹp phạm vi tìm kiếm. | Nhập mã báo cáo không tồn tại hoặc filter không có dữ liệu khớp → Danh sách trống và hiển thị Empty State message: `"Không tìm thấy kết quả"` (CS_01). |
| 4 | BQL KCN/KKT | Thay đổi số bản ghi hiển thị trên phân trang | Thay đổi lựa chọn dropdown phân trang (VD: 10 → 20) → Grid danh sách tự động reload, hiển thị tối đa 20 kỳ hạn báo cáo trên trang và quay về trang 1. | N/A | N/A |

#### B. Business Rules & Validations

| Field / Object | Required | Format / Constraint | Min / Max | Error Message (exact text) |
|----------------|----------|---------------------|-----------|----------------------------|
| Năm (Filter #1 & #5) | No | YearPicker. Mặc định Null (không lọc). | N/A | N/A |
| Trạng thái (Filter #2) | No | Multiple-selection Dropdown. Mặc định `"Tất cả trạng thái"` (không lọc). | N/A | N/A |
| Mã báo cáo (Search filter #3) | No | Textbox. So khớp không phân biệt hoa thường (case-insensitive), tìm kiếm một phần (partial match). Auto-trim khoảng trắng đầu/cuối khi gửi API. | — / 500 ký tự | N/A |
| Trạng thái kỳ (Filter #4) | No | Multiple-selection Dropdown. Mặc định Null (không lọc). | N/A | N/A |
| Phân trang (Pagination) | N/A | Phân trang theo kỳ hạn. | 10 / 20 / 50 / 100 dòng/trang | N/A |

#### C. UI/UX Feedback
* **Loading States:** Hiển thị loading spinner ở giữa vùng grid danh sách khi hệ thống đang tải hoặc lọc dữ liệu.
* **Toast Messages:** Lỗi hệ thống khi tải danh sách (T05) — Tiêu đề: `"Lỗi hệ thống"`, Nội dung: `"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."`.
* **Empty States:** Hiển thị dòng chữ `"Không tìm thấy kết quả"` ở giữa bảng danh sách khi filter/search không có bản ghi nào khớp.
* **Filter Reset:** Khi người dùng xóa hết các tag đã chọn ở Multiple-selection filter, filter tự động dồn Tag và hiển thị lại placeholder mặc định `"Tất cả trạng thái"`.

---

### 6.2 Function: Lập Báo Cáo (UC329-334.2)

#### A. Workflows

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | BQL KCN/KKT | Nhấn nút [Lập báo cáo] tại kỳ hạn ở trạng thái **Trong thời hạn** | Hệ thống mở ra màn hình Lập báo cáo. Bảng mở sẵn 1 dòng trống mặc định. Cột 2 (Dự án) Enabled, các cột 3–8 ở trạng thái Disabled. Nút [Xóa dòng] bị ẩn (do mới có 1 dòng). Nút [Thêm dòng] của 2 Mục luôn enabled. Nút [Hủy], [Xem trước], [Lưu nháp], [Nộp] ở footer hiển thị ở trạng thái enabled. | N/A | N/A |
| 2 | BQL KCN/KKT | Click chọn Dropdown Tên dự án đầu tư (Cột 2) | Hệ thống hiển thị danh sách dự án lấy từ API. Người dùng gõ tên dự án để tìm kiếm nhanh (Instant search). Nhấn chọn dự án. | N/A | API lấy danh sách dự án lỗi → Dropdown trống, hiển thị Toast lỗi hệ thống T05. |
| 3 | BQL KCN/KKT | Chọn xong Dự án đầu tư ở cột 2 | Hệ thống tự động gọi song song 2 API: (1) API Quản lý dự án nội bộ để lấy thông tin KCN, văn bản thành lập, tên nhà đầu tư, quốc tịch; (2) API IRC để lấy vốn ĐTNN, vốn ĐTTN. Điền tự động vào cột 3-8 và khóa Disabled các cột này. Đọc loại hình dự án và tự động chuyển/phân loại dòng đó vào đúng Mục 1 hoặc Mục 2 tương ứng. | N/A | API gọi auto-fill bị lỗi (timeout hoặc server error) → Điền giá trị rỗng vào cột 3-8, chuyển các cột này sang trạng thái **Enabled** cho phép người dùng tự nhập tay, đồng thời hiển thị Toast lỗi hệ thống: `"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."` (T05). |
| 4 | BQL KCN/KKT | Nhấn nút [Thêm dòng...] tại Mục 1 hoặc Mục 2 | Hệ thống thêm 1 dòng mới vào cuối bảng của Mục tương ứng. Cột 2 của dòng mới Enabled, các cột 3-8 Disabled. Hiển thị lại icon [Xóa dòng] cho tất cả các dòng trong bảng của Mục đó (do bảng đã có ≥ 2 dòng). | N/A | N/A |
| 5 | BQL KCN/KKT | Nhấp chuột vào ô Văn bản thu hồi (Cột 9) và nhập ký tự | Ký tự hiển thị trong ô. Hệ thống tự động chuyển chữ thường thành chữ in hoa (auto-uppercase). Block ngay lập tức các khoảng trắng và ký tự đặc biệt ngoài `/` và `-`. | N/A | N/A |
| 6 | BQL KCN/KKT | Nhấp icon [Xóa dòng] ở cột 10 | Hệ thống xóa dòng đó ra khỏi bảng ngay lập tức, phân bổ lại số thứ tự (STT) ở cột 1 tự động tăng từ 1. | N/A | Nếu sau khi xóa bảng chỉ còn lại 1 dòng duy nhất → hệ thống tự động ẩn nút [Xóa dòng] đi. |
| 7a | BQL KCN/KKT | Nhấn nút [Lưu nháp] | Hệ thống thực hiện validate bắt buộc đối với Cột 2 (Dự án) và Cột 9 (Văn bản thu hồi - do là trường nhập tay duy nhất). Nếu hợp lệ → Lưu bản ghi vào DB dưới trạng thái "Lưu nháp". Sinh mã báo cáo. Hiển thị Toast thành công: `"Đã lập báo cáo thành công"` (T01). Điều hướng quay về màn hình Danh sách. | N/A | - **Lỗi rỗng:** Nếu tất cả các trường đều trống (chưa chọn dự án, chưa nhập văn bản thu hồi) → Dừng lưu, hiển thị Toast lỗi: `"Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp"` (T07).<br>- **Lỗi thiếu:** Nếu chọn dự án nhưng bỏ trống cột 9 → Hiển thị lỗi inline màu đỏ bên dưới Cột 9: `"Vui lòng nhập Văn bản thu hồi chủ trương ĐT/GCNĐKĐT"` (V01).<br>- **Lỗi định dạng:** Nhập sai định dạng số công văn ở Cột 9 → Hiển thị lỗi inline V05/V06/V07 tương ứng.<br>- **Lỗi server:** Lưu thất bại do DB/Server lỗi → Toast lỗi hệ thống (T05). |
| 7b | BQL KCN/KKT | Nhấn nút [Nộp báo cáo] | Bước 1: Validate tất cả các trường bắt buộc trên toàn form (Cột 2, Cột 9, và các cột 3-8 nếu người dùng phải nhập tay do API lỗi).<br>Bước 2: Validate định dạng Số công văn ở Cột 9.<br>Bước 3: Nếu hợp lệ → Mở popup xác nhận nộp bản ghi (P01). Người dùng tích vào checkbox xác nhận thông tin chính xác → Nút [Xác nhận] chuyển sang Active. Người dùng nhấn nút [Xác nhận].<br>Bước 4: Lưu dữ liệu vào DB dưới trạng thái "Chờ duyệt" (quy trình >2 bước). Toast thành công: `"Đã nộp báo cáo thành công"` (T02). Điều hướng quay về màn hình Danh sách. | Người dùng nhấn nút [Hủy] hoặc icon (✕) trên popup xác nhận nộp → Đóng popup, giữ nguyên giao diện form lập báo cáo để tiếp tục chỉnh sửa. | - **Lỗi validate:** Nếu phát hiện trường bắt buộc trống hoặc sai định dạng ở Cột 9 → Dừng luồng nộp, không mở popup xác nhận, hiển thị các thông báo lỗi inline màu đỏ tương ứng dưới các trường vi phạm.<br>- **Lỗi bảng rỗng:** Nếu bảng không có bất kỳ dòng dữ liệu nào khi nộp → Hiển thị Toast lỗi: `"Vui lòng nhập ít nhất 1 dòng dữ liệu"` (T15).<br>- **Lỗi quá dòng:** Nếu tổng số dòng vượt quá 500 dòng → Hiển thị Toast lỗi: `"Vượt quá số dòng tối đa cho phép (500)"` (T16).<br>- **Lỗi server:** Gặp lỗi khi gửi API nộp → Hiển thị Toast lỗi hệ thống (T05). |
| 7c | BQL KCN/KKT | Nhấn nút [Hủy] | Hệ thống thực hiện Dirty check form: So sánh dữ liệu hiện tại với lúc load form. | - **Form không dirty (không thay đổi gì):** Hệ thống lập tức đóng form, điều hướng quay về màn hình Danh sách báo cáo mà không hiển thị popup.<br>- **Form dirty (có thay đổi giá trị trường):** Hệ thống kích hoạt Dirty Form Guard → Hiển thị popup cảnh báo `"Dữ liệu chưa được lưu / Bạn có chắc chắn muốn rời khỏi trang này không?"` (P02). Người dùng nhấn **[Đồng ý]** → đóng popup, quay về màn hình Danh sách, hủy bỏ dữ liệu chưa lưu. Người dùng nhấn **[Hủy]** → đóng popup, ở lại form lập báo cáo, giữ nguyên toàn bộ dữ liệu đang nhập dở. | N/A |

#### B. Business Rules & Validations

| Field / Object | Required | Format / Constraint | Min / Max | Error Message (exact text) |
|----------------|----------|---------------------|-----------|----------------------------|
| Tên dự án đầu tư (Cột 2) | Yes | Dropdown chọn 1 giá trị. Instant search. | N/A | `"Vui lòng chọn tên dự án đầu tư"` (V01) |
| Các cột dữ liệu API (Cột 3, 4, 5, 6, 7, 8) | Yes (Chỉ validate khi API lỗi/null phải nhập tay) | - Trường text (Cột 3, 4, 5, 6): Trim khoảng trắng. Max length 500 ký tự.<br>- Trường số (Cột 7, 8): Số dương ≥0, tối đa 1 dấu chấm thập phân, dấu phẩy phân tách hàng nghìn đúng định dạng. Max length 18 ký tự. | — / 500 ký tự (Text)<br>— / 18 ký tự (Số) | - Trống: `"Vui lòng nhập [tên trường]"` (V01)<br>- Số âm: `"Ký tự không hợp lệ. Chỉ chấp nhận chữ số, dấu chấm và dấu phẩy"` (V03)<br>- Số sai định dạng: `"Sai định dạng số."` (V04)<br>- Quá max length: `"[Tên trường] nhập quá ký tự cho phép"` |
| Văn bản thu hồi (Cột 9) | Yes | Nhập tay. Trim khoảng trắng. Định dạng Số công văn: `[Số thứ tự]/[Ký hiệu 1]-[Ký hiệu 2]`. Chữ viết hoa, không chứa khoảng trắng và ký tự đặc biệt ngoài `/` và `-`. | — / 500 ký tự | - Trống: `"Vui lòng nhập Văn bản thu hồi chủ trương ĐT/GCNĐKĐT"` (V01)<br>- Thiếu `/`: `"Số công văn chưa đúng chuẩn, thiếu dấu "/""` (V05)<br>- Thiếu `-`: `"Số công văn chưa đúng chuẩn, thiếu dấu "-""` (V06)<br>- Sai cấu trúc khác: `"Vui lòng nhập lại thông tin"` (V07) |

#### C. UI/UX Feedback
* **Loading auto-fill:** Hiển thị loading icon nhỏ xoay tròn tại dòng bảng đang chọn dự án khi gọi song song 2 API tự động điền dữ liệu.
* **Inline error:** Khi có lỗi validate, trường vi phạm chuyển viền đỏ, hiển thị câu thông báo lỗi bằng chữ màu đỏ ngay bên dưới ô nhập liệu. Lỗi tự biến mất ngay khi người dùng chỉnh sửa hợp lệ.
* **Popup xác nhận nộp (P01):** Tiêu đề: `"Bạn có chắc muốn nộp?"`. Checkbox: `"Tôi đã kiểm tra toàn bộ thông tin đã nhập và xác nhận rằng các thông tin đó là chính xác."`. Nút `[Xác nhận]` mặc định bị Disabled, chỉ chuyển sang Enabled (màu xanh theo theme) sau khi người dùng tích chọn checkbox. Nút `[Hủy]` và icon `(✕)` đóng popup luôn active.
* **Popup hủy (Dirty Form Guard - P02):** Tiêu đề: `"Dữ liệu chưa được lưu"`. Nội dung: `"Bạn có chắc chắn muốn rời khỏi trang này không?"`. Nút `[Đồng ý]` (màu đỏ/xám nổi bật để xác nhận rời) và nút `[Hủy]` (giữ lại trang).

---

### 6.3 Function: Các Tác Vụ Bổ Trợ (UC329-334.3)

#### A. Workflows

| Step | Actor | Action | System Response (Happy Path) | Alternative Flows | Exception & Error Flows |
|------|-------|--------|------------------------------|-------------------|-------------------------|
| 1 | BQL KCN/KKT | Nhấn [Xem chi tiết] tại cột Hành động trên Danh sách | Hệ thống mở ra màn hình Xem chi tiết dạng full-page. Toàn bộ các trường dữ liệu ở trạng thái Disabled (đóng băng). Hiển thị đầy đủ thông tin của bản ghi. Footer hiển thị nút [Chỉnh sửa] (nếu bản ghi ở trạng thái Lưu nháp hoặc YCCS) và nút [Hủy]. | N/A | Lỗi kết nối server không lấy được chi tiết → Toast lỗi hệ thống (T05). |
| 2 | BQL KCN/KKT | Nhấn [Chỉnh sửa] (từ màn Xem chi tiết hoặc cột Hành động Danh sách) | Hệ thống mở ra giao diện form Chỉnh sửa báo cáo, điền sẵn toàn bộ dữ liệu cũ của bản ghi. Các cột API (3-8) giữ trạng thái Disabled (CMR_12). Các trường cột 2, cột 9 và nút thêm/xóa dòng Enabled cho phép chỉnh sửa. | N/A | N/A |
| 3 | BQL KCN/KKT | Thao tác trên form Chỉnh sửa của bản ghi đang ở trạng thái **Yêu cầu chỉnh sửa** | Khi form chưa có thay đổi nào so với lúc load (chưa dirty) → Hệ thống khóa **Disabled** cả 2 nút [Lưu nháp] và [Nộp báo cáo] ở footer form. Hover vào nút hiển thị tooltip hướng dẫn chỉnh sửa. | Ngay khi người dùng sửa ít nhất 1 ký tự/lựa chọn (form dirty) → Hệ thống tự động chuyển cả 2 nút sang **Enabled** cho phép click lưu/nộp. | N/A |
| 4 | BQL KCN/KKT | Nhấn [Xem vòng đời] tại cột Hành động trên Danh sách | Hệ thống mở một popup Timeline ghi nhận nhật ký hoạt động (Lifecycle Log) của bản ghi báo cáo: Tên người lập/thao tác, hành động thực hiện (Khởi tạo, Sửa, Nộp, Yêu cầu chỉnh sửa, Tiếp nhận), thời gian thực hiện (giờ phút ngày tháng). Sắp xếp theo trình tự thời gian từ cũ → mới. | N/A | Lỗi không lấy được log → Toast lỗi hệ thống (T05). |
| 5 | BQL KCN/KKT | Nhấn [In] tại cột Hành động trên Danh sách | Hệ thống xuất dữ liệu ra file PDF in-memory, mở tab Print Preview PDF của trình duyệt kèm theo hộp thoại lựa chọn máy in mặc định. | Người dùng hủy in trên hộp thoại → đóng hộp thoại, tab preview giữ nguyên. | N/A |
| 6 | BQL KCN/KKT | Nhấn [Xuất báo cáo] tại cột Hành động trên Danh sách | Hệ thống kết xuất dữ liệu bản ghi ra file định dạng Word (.docx) theo đúng mẫu biểu quy định. Tự động tải xuống thư mục download của người dùng. Hiển thị Toast thành công: `"Đã xuất báo cáo thành công"` (T04). | N/A | Xuất file thất bại do lỗi hệ thống → Toast lỗi hệ thống (T05). |
| 7 | BQL KCN/KKT | Nhấn [Xóa] tại cột Hành động trên Danh sách (bản ghi trạng thái Lưu nháp và chưa từng nộp) | Hệ thống mở popup xác nhận xóa bản ghi (P04) với câu hỏi: `"Bạn có chắc chắn muốn xóa báo cáo này?"`. Người dùng nhấn **[Đồng ý]**. Hệ thống thực hiện xóa bản ghi trong DB, đóng popup, reload lại danh sách và hiển thị Toast thành công: `"Xóa báo cáo thành công"` (T08). | Người dùng nhấn **[Hủy]** trên popup → đóng popup, bản ghi được giữ nguyên trên danh sách không bị xóa. | Gặp lỗi DB khi thực hiện xóa → Toast lỗi hệ thống (T05). |

#### B. Business Rules & Validations

##### Rule 1: Action Mapping theo trạng thái bản ghi (CMR_03)
Hệ thống hiển thị các nút thao tác tại cột Hành động dựa trên trạng thái của bản ghi như sau:
* **Bản ghi trạng thái [Lưu nháp]:** Hiển thị đầy đủ: [Nộp], [Chỉnh sửa], [Xóa] (chỉ hiển thị nếu chưa từng nộp), [Xem chi tiết], [Xem vòng đời], [In], [Xuất báo cáo].
* **Bản ghi trạng thái [Chờ duyệt] hoặc [Đã tiếp nhận]:** Chỉ hiển thị: [Xem chi tiết], [Xem vòng đời], [In], [Xuất báo cáo]. Quyền sửa đổi bị khóa vĩnh viễn.
* **Bản ghi trạng thái [Yêu cầu chỉnh sửa]:** Hiển thị: [Chỉnh sửa], [Xem chi tiết], [Xem vòng đời], [In], [Xuất báo cáo]. Nút [Nộp] hiển thị trên danh sách nhưng mặc định bị Disabled, chỉ Enabled sau khi người dùng đã vào Chỉnh sửa báo cáo, sửa dữ liệu và Lưu nháp thành công (CMR_14). Nút Xóa bị ẩn hoàn toàn (do bản ghi đã từng được nộp lên hệ thống, có log lịch sử).

##### Rule 2: Điều kiện Xóa bản ghi (CF_08 - Lifecycle Lock)
* Chỉ cho phép xóa bản ghi ở trạng thái **Lưu nháp** VÀ bản ghi đó **chưa từng được nộp** lên hệ thống lần nào.
* Nếu bản ghi được chuyển từ trạng thái "Yêu cầu chỉnh sửa" về "Lưu nháp" sau khi bấm [Lưu nháp] ở màn chỉnh sửa → Nút [Xóa] vẫn bị ẩn vĩnh viễn để bảo toàn tính toàn vẹn dữ liệu (Lifecycle Lock).

##### Rule 3: Bảo toàn trạng thái khi Lưu nháp trong form Chỉnh sửa (CF_03)
* Khi chỉnh sửa bản ghi đang ở trạng thái **Lưu nháp** → nhấn [Lưu nháp] → trạng thái giữ nguyên **Lưu nháp**.
* Khi chỉnh sửa bản ghi đang ở trạng thái **Yêu cầu chỉnh sửa** → nhấn [Lưu nháp] → trạng thái giữ nguyên **Yêu cầu chỉnh sửa**.

##### Rule 4: Disable nút hành động khi chưa dirty ở trạng thái YCCS (CMR_14)
* **Form Chỉnh sửa (CF_03):** Nếu trạng thái cũ là YCCS, khi mở form ra, nút [Nộp báo cáo] và [Lưu nháp] mặc định bị Disabled. Chuyển sang Enabled ngay khi người dùng có thay đổi ít nhất 1 trường (form dirty). Hover hiện tooltip tương ứng: `"Vui lòng chỉnh sửa ít nhất một trường thông tin trước khi nộp/lưu nháp."`
* **Màn hình Danh sách (CF_09):** Nút [Nộp] tại cột hành động của dòng bản ghi YCCS mặc định bị Disabled. Hover hiện tooltip: `"Vui lòng chỉnh sửa báo cáo trước khi nộp lại."`. Nút này chỉ Enabled sau khi người dùng đã chỉnh sửa form, lưu nháp thành công.

#### C. UI/UX Feedback
* **Toast Messages:**
  * Xuất báo cáo thành công (T04) — Tiêu đề: `"Thành công"`, Nội dung: `"Đã xuất báo cáo thành công"`.
  * Xóa báo cáo thành công (T08) — Tiêu đề: `"Thành công"`, Nội dung: `"Xóa báo cáo thành công"`.
  * Chỉnh sửa thành công (T03) — Tiêu đề: `"Thành công"`, Nội dung: `"Đã chỉnh sửa báo cáo thành công"`.
  * Lỗi hệ thống (T05) — Tiêu đề: `"Lỗi hệ thống"`, Nội dung: `"Không thể kết nối đến hệ thống. Vui lòng thử lại sau."`.
* **Popup xác nhận xóa (P04):** Không có tiêu đề. Nội dung: `"Bạn có chắc chắn muốn xóa báo cáo này?"`. Nút `[Đồng ý]` (màu đỏ) và nút `[Hủy]` (màu xám).
* **Tooltip nút bị khóa (YCCS):** Hiển thị tooltip dạng tooltip banner màu tối chữ trắng nhỏ khi hover vào nút [Nộp] / [Lưu nháp] đang bị mờ (Disabled).

---

## 7. Functional Integration Analysis

| Trigger Function / Action | Impact Analysis (Cross-function influence) | Data Consistency Verification |
|---------------------------|--------------------------------------------|-------------------------------|
| Chọn dự án đầu tư ở Cột 2 (Lập/Sửa BC) | Ảnh hưởng trực tiếp: Hệ thống tự động gọi song song 2 API để auto-fill cột 3-8 và tự động phân loại dồn dòng bản ghi vào đúng Mục 1 hoặc Mục 2 tương ứng trên giao diện. | Verify: Thông tin hiển thị ở cột 3-8 khớp chính xác với kết quả trả về của API nội bộ và API IRC. Phân nhóm Mục 1/Mục 2 đúng theo loại hình dự án đã cấu hình. |
| API gọi tự động bị lỗi/null (Lập/Sửa BC) | Ảnh hưởng trực tiếp: Chuyển trạng thái cột 3-8 sang Enabled cho người dùng tự nhập tay để tránh chặn luồng. | Verify: Khi API timeout hoặc lỗi mạng → Các trường cột 3-8 cho phép focus và nhập chữ/số bình thường, hiển thị Toast lỗi hệ thống T05. |
| Lưu nháp báo cáo thành công | Ảnh hưởng: Bản ghi báo cáo mới xuất hiện trên giao diện danh sách tại đúng Kỳ hạn tương ứng. Mã báo cáo được sinh tự động. Cột hành động hiển thị các nút thao tác theo trạng thái Lưu nháp. | Verify: Bản ghi hiển thị đúng kỳ hạn. Mã báo cáo theo pattern `EZ_2116HQLKKT_[ID]`. Ngày cập nhật = thời gian lưu thực tế. |
| Nộp báo cáo thành công | Ảnh hưởng: Trạng thái bản ghi chuyển sang "Chờ duyệt" (quy trình >2 bước). Cột Hành động trên danh sách thay đổi (ẩn hoàn toàn các nút Nộp, Chỉnh sửa, Xóa; chỉ giữ Xem chi tiết, Xem vòng đời, In, Xuất báo cáo). Nhật ký hoạt động ghi nhận sự kiện nộp. | Verify: Trạng thái hiển thị đúng "Chờ duyệt" trên danh sách. Các nút Sửa/Nộp/Xóa bị ẩn/khóa vĩnh viễn. Xem vòng đời ghi nhận thêm sự kiện Nộp. |
| Chỉnh sửa báo cáo thành công (Lưu nháp) | Ảnh hưởng: Cập nhật dữ liệu mới của bản ghi trong DB. Trạng thái bản ghi bảo toàn. Ngày cập nhật hiển thị trên danh sách thay đổi thành thời điểm lưu mới nhất. | Verify: Màn hình Danh sách và Xem chi tiết hiển thị đúng dữ liệu mới sửa. Ngày cập nhật được cập nhật chính xác theo realtime. |
| Xóa báo cáo thành công | Ảnh hưởng: Bản ghi bị xóa khỏi DB và biến mất khỏi danh sách hiển thị. Số lượng bản ghi trong kỳ hạn đó giảm đi 1, phân trang tự động cập nhật lại. | Verify: Bản ghi không còn xuất hiện trên giao diện. Thông tin text phân trang (Hiển thị start-end/total) cập nhật giảm số lượng bản ghi đi 1. |
| Thay đổi thời gian thực tế hệ thống (Realtime) | Ảnh hưởng trực tiếp đến Trạng thái kỳ hạn báo cáo: Ẩn/Hiện nút [Lập báo cáo] và [Nhập từ file] tại Khung kỳ hạn. | Verify: Kỳ hạn chuyển từ "Trong thời hạn" → "Qua kỳ báo cáo" → các nút [Lập báo cáo] và [Nhập từ file] lập tức biến mất trên giao diện. |

**Status:** ✅ Complete

---

## 8. Acceptance Criteria

| AC # | Scenario | Given (precondition) | When (user action) | Then (expected result) |
|------|----------|----------------------|---------------------|------------------------|
| AC-01 | Xem danh sách - Happy Path | BQL đã đăng nhập, có quyền truy cập | Mở màn hình Danh sách báo cáo | Hiển thị màn danh sách, bộ lọc mặc định (Năm = Null, Trạng thái = "Tất cả trạng thái"), các kỳ hạn báo cáo ở trạng thái Collapse. |
| AC-02 | Expand kỳ hạn báo cáo | Kỳ hạn đang hiển thị trên danh sách, có báo cáo | Click mũi tên expand kỳ hạn | Hiển thị danh sách các báo cáo đã lập bên trong kỳ hạn, sắp xếp từ mới → cũ theo ngày cập nhật. |
| AC-03 | Lọc theo trạng thái báo cáo | Danh sách hiển thị nhiều báo cáo có các trạng thái khác nhau | Chọn trạng thái "Lưu nháp" ở filter Trạng thái | Grid danh sách cập nhật ngay lập tức (real-time), chỉ hiển thị các báo cáo có trạng thái "Lưu nháp". |
| AC-04 | Tìm kiếm nhanh theo mã báo cáo | Danh sách có bản ghi báo cáo | Nhập mã báo cáo vào ô tìm kiếm | Hệ thống tự động lọc và hiển thị báo cáo khớp mã ngay khi gõ ký tự (real-time, case-insensitive). |
| AC-05 | Tìm kiếm không có kết quả | Danh sách có bản ghi | Nhập mã báo cáo không tồn tại vào ô tìm kiếm | Grid danh sách trống và hiển thị thông điệp Empty State: `"Không tìm thấy kết quả"`. |
| AC-06 | Ẩn/Hiện nút Lập BC - Trong thời hạn | Kỳ hạn ở trạng thái "Trong thời hạn" (dựa trên realtime hệ thống) | Quan sát Khung Kỳ hạn | Nút [Lập báo cáo] và [Nhập từ file] hiển thị rõ ràng trên giao diện. |
| AC-07 | Ẩn/Hiện nút Lập BC - Qua kỳ / Chưa tới | Kỳ hạn ở trạng thái "Qua kỳ báo cáo" hoặc "Chưa tới hạn" | Quan sát Khung Kỳ hạn | Nút [Lập báo cáo] và [Nhập từ file] bị ẩn hoàn toàn khỏi giao diện. |
| AC-08 | Lập BC - Chọn dự án + API auto-fill thành công | Form Lập BC mở ra, bảng có 1 dòng trống mặc định | Click chọn 1 dự án đầu tư ở Dropdown Cột 2 | Hệ thống gọi song song 2 API lấy dữ liệu auto-fill điền vào cột 3-8, khóa Disabled các cột này, và tự động chuyển dòng đó vào đúng Mục 1 hoặc Mục 2 tương ứng. |
| AC-09 | Lập BC - API auto-fill bị lỗi / trả về null | Form Lập BC mở ra, chọn dự án ở cột 2 | Gọi API auto-fill bị lỗi timeout hoặc API trả về rỗng | Hiển thị Toast lỗi hệ thống T05. Các cột 3-8 giữ trống và tự động chuyển sang trạng thái **Enabled** cho phép người dùng tự click nhập tay. |
| AC-10 | Lập BC - Thêm dòng mới | Form Lập BC đang mở | Nhấn nút [Thêm dòng mục...] ở Mục 1 hoặc Mục 2 | Thêm 1 dòng trống mới ở cuối bảng của Mục tương ứng. Cột 2 dòng mới Enabled, cột 3-8 Disabled. Icon [Xóa dòng] hiển thị trên tất cả các dòng (bảng đã có ≥ 2 dòng). |
| AC-11 | Lập BC - Xóa dòng bảng động | Bảng nhập liệu đang hiển thị ≥ 2 dòng | Click icon [Xóa dòng] ở cột 10 của 1 dòng | Dòng đó bị xóa lập tức khỏi bảng mà không có popup xác nhận. Số thứ tự (STT) ở cột 1 tự động cập nhật lại tăng từ 1. |
| AC-12 | Lập BC - Ẩn nút Xóa dòng | Bảng chỉ còn 1 dòng duy nhất | Quan sát dòng bảng | Icon [Xóa dòng] ở cột 10 bị ẩn đi hoàn toàn. |
| AC-13 | Lập BC - Lưu nháp thành công | Đã chọn dự án ở cột 2, đã nhập Văn bản thu hồi ở cột 9 đúng định dạng | Nhấn nút [Lưu nháp] ở footer | Hiển thị Toast thành công: `"Đã lập báo cáo thành công"` (T01). Bản ghi được lưu ở trạng thái "Lưu nháp" với mã báo cáo tự sinh `EZ_2116HQLKKT_[ID]`. Điều hướng về Danh sách. |
| AC-14 | Lập BC - Lưu nháp khi form rỗng | Form mới tinh chưa nhập bất kỳ dữ liệu nào | Nhấn nút [Lưu nháp] | Dừng lưu, hiển thị Toast lỗi: `"Bạn cần nhập dữ liệu cho trường thông tin trước khi lưu nháp"` (T07). |
| AC-15 | Lập BC - Lưu nháp thiếu trường bắt buộc | Đã chọn dự án ở cột 2, bỏ trống Văn bản thu hồi ở cột 9 | Nhấn nút [Lưu nháp] | Dừng lưu, hiển thị lỗi inline đỏ dưới Cột 9: `"Vui lòng nhập Văn bản thu hồi chủ trương ĐT/GCNĐKĐT"`. |
| AC-16 | Lập BC - Nộp báo cáo thành công | Form đã nhập đầy đủ dữ liệu bắt buộc và đúng định dạng | Nhấn nút [Nộp báo cáo] ở footer | Hiển thị popup xác nhận nộp P01. Checkbox xác nhận được tích → Nút [Xác nhận] active. Người dùng click [Xác nhận] → Lưu DB dưới trạng thái "Chờ duyệt", hiển thị Toast thành công T02 và điều hướng về Danh sách. |
| AC-17 | Lập BC - Nộp báo cáo khi thiếu trường bắt buộc | Cột 9 (Văn bản thu hồi) bị bỏ trống | Nhấn nút [Nộp báo cáo] ở footer | Dừng luồng nộp, không mở popup xác nhận. Hiển thị lỗi inline đỏ dưới Cột 9: `"Vui lòng nhập Văn bản thu hồi chủ trương ĐT/GCNĐKĐT"`. |
| AC-18 | Lập BC - Validate định dạng Số công văn | Cột 9 nhập thiếu dấu `/` (VD: `01QĐ-UBND`) | Nhấn [Lưu nháp] hoặc [Nộp báo cáo] | Dừng luồng, hiển thị lỗi inline đỏ dưới Cột 9: `"Số công văn chưa đúng chuẩn, thiếu dấu "/""` (V05). |
| AC-19 | Lập BC - Hủy khi form không dirty | Mở form mới, chưa thay đổi bất kỳ trường nào | Nhấn nút [Hủy] ở footer | Đóng form lập báo cáo và điều hướng lập tức quay về màn hình Danh sách mà không hiển thị popup cảnh báo. |
| AC-20 | Lập BC - Hủy khi form dirty (Dirty Form Guard) | Người dùng đã nhập dữ liệu (form dirty) nhưng chưa lưu | Nhấn nút [Hủy] ở footer | Kích hoạt Dirty Form Guard → Hiển thị popup cảnh báo P02. Click **[Đồng ý]** → quay về Danh sách, hủy dữ liệu. Click **[Hủy]** → đóng popup, giữ nguyên form. |
| AC-21 | Xem chi tiết báo cáo | Bản ghi báo cáo đã tồn tại | Click nút [Xem chi tiết] | Mở màn Xem chi tiết full-page. Toàn bộ các trường dữ liệu ở trạng thái Disabled (Read-only). Nút [Chỉnh sửa] chỉ xuất hiện nếu trạng thái bản ghi là Lưu nháp hoặc YCCS. |
| AC-22 | Chỉnh sửa - Bảo toàn trạng thái khi lưu nháp | Bản ghi đang ở trạng thái YCCS, người dùng đã vào form sửa dữ liệu | Nhấn nút [Lưu nháp] ở footer form sửa | Lưu cập nhật thành công, hiển thị Toast T03. Trạng thái bản ghi được bảo toàn là **Yêu cầu chỉnh sửa**. |
| AC-23 | Chỉnh sửa (YCCS) - Khóa nút khi chưa dirty | Bản ghi đang ở trạng thái YCCS, người dùng vừa mở form chỉnh sửa | Quan sát footer form | Nút [Lưu nháp] và [Nộp báo cáo] mặc định bị Disabled (mờ). Hover hiện tooltip tương ứng. Nút chỉ Enabled sau khi người dùng sửa ít nhất 1 ký tự (form dirty). |
| AC-24 | Xóa báo cáo thành công | Bản ghi đang ở trạng thái Lưu nháp và chưa từng được nộp lần nào | Click nút [Xóa] ở cột hành động → Click **[Đồng ý]** trên popup P04 | Bản ghi bị xóa khỏi danh sách, hiển thị Toast thành công T08. Phân trang cập nhật giảm 1 bản ghi. |
| AC-25 | Xóa báo cáo - Lifecycle Lock | Bản ghi đang ở trạng thái Lưu nháp nhưng đã từng được nộp trước đó (sau khi bị YCCS) | Quan sát cột Hành động trên Danh sách | Nút [Xóa] bị ẩn hoàn toàn để bảo vệ lịch sử dữ liệu (Lifecycle Lock). |
| AC-26 | Xuất báo cáo thành công | Bản ghi báo cáo đã tồn tại | Click nút [Xuất báo cáo] ở cột hành động | Tải xuống file .docx chứa nội dung báo cáo thành công, hiển thị Toast thành công T04. |

**Status:** ✅ Complete

---

## 9. Non-functional Requirements

| Category | Requirement | Source / Reference |
|----------|-------------|-------------------|
| Performance | Bộ lọc (Năm, Trạng thái, Trạng thái kỳ) và ô tìm kiếm Mã báo cáo bắt buộc phải tự động lọc và hiển thị kết quả ngay lập tức (real-time filtering), không có độ trễ UI gây cảm giác gián đoạn. | UC329-334.1 |
| Performance | Thời gian gọi API tự động điền dữ liệu (gọi song song API nội bộ + API IRC) bắt buộc phải phản hồi nhanh (SLA < 3 giây). | Giả định hệ thống |
| Usability | Tất cả các thông báo Toast thành công (T01, T02, T03, T04, T08) phải hiển thị ở góc trên bên phải màn hình và tự động ẩn đi sau 3–5 giây để tránh làm phiền người dùng. | CMR_06 |
| Usability | Giao diện phải tuân thủ chuẩn phím tắt Tab Navigation: Nhấn Tab chuyển sang field tiếp theo, Shift+Tab quay lại field trước theo thứ tự từ trái qua phải, trên xuống dưới. | CMR_18 |
| Security | Kiểm soát quyền truy cập chặt chẽ: Chỉ người dùng thuộc Ban Quản lý các KCN, KKT mới có quyền lập, nộp, sửa, xóa báo cáo này. Các nhà đầu tư thành viên không được phép xem hay thao tác trên Admin site. | Metadata, Q1 Backlog |
| Data Integrity | Mã báo cáo sinh ra phải tuân thủ nghiêm ngặt quy tắc đặt tên tiền tố phân hệ quản lý KCN, KKT: `EZ_2116HQLKKT_[ID]` và phải là duy nhất trên toàn hệ thống (Global Unique). | CMR_09 |

**Status:** ⚡ Partial (Do tài liệu gốc không có phần NFR chính thức, các yêu cầu trên được QC Agent đúc rút và chuẩn hóa từ ngữ cảnh nghiệp vụ chung của hệ thống MBFS).

---

## 10. Audit Summary

| # | Knowledge Area | Max Pts | Score | Status |
|---|---|---|---|---|
| 1 | Feature Identity | 5 | 5/5 | ✅ |
| 2 | Objective & Scope | 5 | 5/5 | ✅ |
| 3 | Actors & User Roles | 10 | 10/10 | ✅ |
| 4 | Preconditions & Postconditions | 10 | 10/10 | ✅ |
| 5 | UI Object Inventory & Mapping | 15 | 15/15 | ✅ |
| 6 | Object Attributes & Behavior Definition | 20 | 20/20 | ✅ |
| 7 | Functional Logic & Workflow Decomposition | 20 | 20/20 | ✅ |
| 8 | Functional Integration Analysis | 10 | 10/10 | ✅ |
| 9 | Acceptance Criteria | 10 | 10/10 | ✅ |
| 10 | Non-functional Requirements | 5 | 4/5 | ⚡ |
| **Total** | | **110** | **109/110** | **99.1/100** |

* **Quy đổi điểm hệ 100:** `Final Score = round((109 / 110) * 100, 1) = 99.1 / 100`
* **Nhận định chung:** Tài liệu cực kỳ chi tiết, cấu trúc rõ ràng, logic nghiệp vụ chặt chẽ, đầy đủ tham chiếu và inlined chuẩn xác các quy tắc nghiệp vụ chung (CMR) cũng như danh mục Toast/Alert/Popup. Đạt điểm số xuất sắc.

---

## 11. Unified Gap & Question Report

| ID | Priority | Ref | Question | Why It Matters | Status |
|----|----------|-----|----------|----------------|--------|
| Q4 | Low | "Hệ thống tự động phân loại bản ghi vào mục này nếu dự án thuộc loại hình..." | Thuộc tính "loại hình dự án" được xác định từ API nào? Nếu API không trả về thuộc tính này hoặc trả về giá trị không xác định, hệ thống xử lý thế nào? **BA trả lời:** Hiện assumtion lấy từ IRC, chưa có tài liệu API nên chưa có thông tin định dạng dữ liệu → sẽ cập nhật bổ sung sau. | Cần test edge case: dự án không xác định loại hình → phân loại vào mục nào? Có hiển thị lỗi không? Chờ tài liệu API bổ sung để hoàn thiện. | Open |

---

## 12. Change Log

| Version | Date | Author | Summary of Changes |
|---------|------|--------|--------------------|
| v1 | 2026-05-07 | QC Agent | First audit — Đạt điểm số **91.8/100** (Conditionally Ready). Phát hiện 7 câu hỏi mở. |
| v2 | 2026-05-21 | Antigravity QC Agent | Re-audit — Đạt điểm số **99.1/100** (Ready).<br>- Tích hợp các câu trả lời chính thức của BA cho các câu hỏi mở Q1, Q3, Q5, Q6 vào tài liệu audit.<br>- Cập nhật UI Object Inventory và Attributes với cơ chế Thêm dòng bằng 2 nút B0a, B0b và nút Xem chi tiết.<br>- Chuẩn hóa quy tắc sinh mã báo cáo mới (`EZ_2116HQLKKT_[ID]`).<br>- Cập nhật Precondition & Postcondition chi tiết theo SRS v1.5.<br>- Inline chi tiết các thông điệp Toast/Alert/Popup (T01-T08, T15, P01, P02, P04) và các quy tắc nghiệp vụ chung hệ thống (CMR_03, CMR_04, CMR_05, CMR_06, CMR_07, CMR_10, CMR_12, CMR_13, CMR_14, CMR_15, CMR_16, CMR_18). |
